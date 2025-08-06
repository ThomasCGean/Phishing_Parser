# notifier.py

import smtplib
from email.message import EmailMessage
from config import EMAIL_ADDRESS, EMAIL_PASSWORD

def send_quarantine_alert(subject: str, confidence: float):
    """
    Sends an email notification to the user when a phishing email is quarantined.
    """
    try:
        msg = EmailMessage()
        msg["Subject"] = "⚠️ Phishing Email Quarantined"
        msg["From"] = EMAIL_ADDRESS
        msg["To"] = EMAIL_ADDRESS  # self-send

        msg.set_content(f"""
A new phishing email was detected and quarantined.

Subject: {subject}
Confidence: {confidence:.2f}

You can review it in your 'Phishing' folder.

- Phishing Detection Bot
        """)

        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            smtp.send_message(msg)
        print("📧 Notification email sent.")
    except Exception as e:
        print(f"❌ Failed to send quarantine notification: {e}")
