# RedPhish – AI-Powered Email Phishing Detection Tool

RedPhish is a proof-of-concept phishing email detection tool that uses a fine-tuned **DistilBERT** model to classify incoming emails as **phishing** or **legitimate**.  
Suspicious emails are automatically quarantined, and optional email notifications can be sent to alert the user.

---

## 📌 Features
- **Deep Learning Detection** – Uses a fine-tuned DistilBERT model trained on Enron (legitimate) and phishing datasets.
- **Inbox Integration** – Connects to Gmail via IMAP to retrieve and process emails.
- **Automatic Quarantine** – Moves suspected phishing emails to a designated folder.
- **User Notification** – Sends email alerts when suspicious emails are quarantined.
- **Cross-Platform** – Runs on Windows, macOS, and Linux with Python installed.

---

## 📂 Project Structure

redphish/
│
├── main.py # Entry point – pulls emails, runs model inference, quarantines as needed
├── activate.py # Single script to make RedPhish run with the current user_config settings
├── email_reader.py # Handles connecting to and retrieving emails from Gmail
├── preprocess.py # Cleans email subject/body text for model compatibility
├── inference.py # Loads trained DistilBERT model and runs predictions
├── quarantine.py # Moves suspicious emails to quarantine folder
├── notifier.py # Sends user notifications for quarantined emails
├── config_loader.py # Loads config from config.py or example_config.py
├── user_config.py # Template for configuration
├── requirements.txt # Python dependencies
└── models/distilbert_phishing/best # Trained model files, detection engine goes here

TO WORK WITH GMAIL:

1. Enable IMAP in Gmail settings.

2. Enable 2-Step Verification and create an App Password.

3. Save the app password for use in configuration, make sure to paste without spaces.

## USING AND DEPLOYING THIS TOOL ##

Clone this repository to your desired location, ensure Python 3.8+ is installed

Install requirements listed in requirements.txt: 
pip install -r requirements.txt

Place any DistilBERT model of your choice into the folder models/distilBERT_phishing/best
(Original pre-trained model available upon request)

Fill out your email information in user_config.py, then activate activate.py: 
python activate.py

This will:

    -Connect to Gmail

    -Retrieve recent emails

    -Preprocess subject and body

    -Run model inference

    -Move suspected phishing emails to quarantine

    -Send notifications (if an email is quarantined)

    -Keep running until stopped