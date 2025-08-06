# action_handler.py

from config import PHISHING_FOLDER
from notifier import send_quarantine_alert

def handle_phishing_email(client, uid, subject, result):
    print("🚨 Phishing email detected:")
    print(f"  ➤ Subject: {subject}")
    print(f"  ➤ Confidence: {result['confidence']:.2f}")

    try:
        client.create_folder(PHISHING_FOLDER)
    except:
        pass  # Folder may already exist

    client.copy(uid, PHISHING_FOLDER)
    client.delete_messages([uid])
    client.expunge()
    print("  ✅ Moved to quarantine folder.")

    # 🔔 Send notification
    send_quarantine_alert(subject, result["confidence"])

def handle_legitimate_email(subject, result):
    """
    Optionally log legitimate emails.
    """
    print("✅ Legitimate email:")
    print(f"  ➤ Subject: {subject}")
    print(f"  ➤ Confidence: {result['confidence']:.2f}\n")
