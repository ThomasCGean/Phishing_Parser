# THIS CONFIG FILE BECOMES ACTIVE WHEN RENAMED TO config.py
EMAIL_HOST = "imap.gmail.com"                       # Hostname for Gmail clients
EMAIL_ADDRESS = "<YOUR_EMAIL_ADDRESS_HERE>"
EMAIL_PASSWORD = "<APP_PASSWORD_FOR_YOUR_EMAIL>"    # 2FA is required to generate an app password for Gmail
INBOX_FOLDER = "INBOX"                              # Default name, can be changed to your preferred folder
PHISHING_FOLDER = "Phishing"                        # Must create this folder (AKA Label, for Gmail)
MODEL_DIR = "./models/distilbert_phishing/best"     # Default path to model
CONFIDENCE_THRESHOLD = 0.5                          # >0.5 is marked Phishing, <0.5 is marked Legit
MAX_EMAILS_PER_RUN = 5                              # Number of emails pulled every 60 seconds