# JLPTFlashcards

A web application designed to help you study for the Japanese Language Proficiency Test (JLPT) by creating and managing flashcards. Users can upload CSV files with vocabulary, automatically generate flashcard sets, study interactively using these flashcards, and track their progress over time.

## Features

	•	CSV Upload: Upload your vocabulary files in CSV format to create flashcard sets.
	•	Interactive Study Mode: Engage with flashcards using “Know” and “Don’t Know” buttons to track your progress.
	•	Progress Tracking: View and manage your study sessions and flashcard sets.
	•	History Feature: Keep track of all uploaded flashcard sets, allowing you to revisit and study previous sessions.
	•	Clean UI: Simple and intuitive user interface for easy navigation.

### Home Page 
![image](https://github.com/user-attachments/assets/27f85ae9-f78e-4fdd-90b8-51c160d8177a)

### Flash Cards 
<img width="1095" alt="image" src="https://github.com/user-attachments/assets/d355bd09-89f8-462a-bd7c-084a9001808d">


## Structure
```
JLPTFlashcards/
│
├── app.py               # Main Flask application file
├── Dockerfile           # Dockerfile to create a Docker image
├── docker-compose.yml   # Docker Compose configuration file
├── models.py            # Database models
├── requirements.txt     # Python dependencies
├── templates/           # Directory for HTML templates
│   ├── index.html       # Home page template
│   ├── flashcard.html   # Flashcard viewing template
│   └── result.html      # Result display template
├── static/              # Directory for static files (CSS, JS, images)
│   └── style.css        # Custom CSS for the application
└── uploads/             # Directory where uploaded CSV files are stored 
```
## Getting Started

1.	Clone the repository:
 ```
git clone https://github.com/jakariaemon/JLPTFlashcards.git
cd JLPTFlashcards
``` 
2. Build and run
```
docker-compose up --build
```
3. Access 
```
http://localhost:8000 
``` 

## Usage

	1.	Upload CSV Files: Navigate to the home page and upload your CSV file containing the vocabulary.
	2.	Start Studying: Once the file is uploaded, the flashcard session will begin automatically.
	3.	Track Progress: Use the “Know” and “Don’t Know” buttons to track which vocabulary you are familiar with.
	4.	View History: Access previously uploaded flashcard sets from the history section on the home page, allowing you to revisit and study previous sessions.

## CSV File Format

Your CSV file should have three columns in the following order:

	1.	Hiragana: The Japanese reading in hiragana.
	2.	Kanji: The kanji characters (if applicable).
	3.	English: The English translation.

### Example 
```
Hiragana, Kanji, English 
おきます,起きます,get up
ねます,寝ます,sleep
```

## License

This project is licensed under the MIT License. 
