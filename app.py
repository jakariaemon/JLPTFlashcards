from flask import Flask, render_template, request, redirect, url_for
import os
import pandas as pd
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///flashcards.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOAD_FOLDER'] = 'uploads'

if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

db = SQLAlchemy(app)

class FlashcardSet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    filename = db.Column(db.String(150), nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

    def __init__(self, name, filename):
        self.name = name
        self.filename = filename

vocab_list = []
current_index = 0
score = 0

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files.get('file')
        set_name = request.form.get('set_name')

        if file and set_name and file.filename.endswith('.csv'):
            filename = set_name.replace(" ", "_") + ".csv"
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)

            new_set = FlashcardSet(name=set_name, filename=filename)
            db.session.add(new_set)
            db.session.commit()
            return redirect(url_for('flashcard', set_id=new_set.id))

    flashcard_sets = FlashcardSet.query.order_by(FlashcardSet.timestamp.desc()).all()
    return render_template('index.html', flashcard_sets=flashcard_sets)

@app.route('/flashcard/<int:set_id>', methods=['GET', 'POST'])
def flashcard(set_id):
    global vocab_list, current_index, score
    flashcard_set = FlashcardSet.query.get_or_404(set_id)
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], flashcard_set.filename)
    df = pd.read_csv(file_path)
    vocab_list = df.to_dict(orient='records')

    if request.method == 'POST':
        action = request.form.get('action')
        if action == 'known':
            score += 1
        current_index += 1

        if current_index >= len(vocab_list):
            return redirect(url_for('result', set_id=set_id))

    return render_template('flashcard.html', vocab=vocab_list[current_index], index=current_index, total=len(vocab_list), set_name=flashcard_set.name, set_id=set_id)

@app.route('/result/<int:set_id>')
def result(set_id):
    flashcard_set = FlashcardSet.query.get_or_404(set_id)
    return render_template('result.html', score=score, total=len(vocab_list), set_name=flashcard_set.name)

@app.route('/delete/<int:set_id>', methods=['POST'])
def delete_set(set_id):
    flashcard_set = FlashcardSet.query.get_or_404(set_id)
    try:
        os.remove(os.path.join(app.config['UPLOAD_FOLDER'], flashcard_set.filename))
    except OSError as e:
        print(f"Error deleting file: {e}")

    db.session.delete(flashcard_set)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/reset')
def reset():
    global vocab_list, current_index, score
    vocab_list = []
    current_index = 0
    score = 0
    return redirect(url_for('index'))

if __name__ == "__main__":
    with app.app_context():
        db.create_all()

    app.run(host='0.0.0.0', port=8000, debug=True)