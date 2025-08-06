# action_handler.py

from config import PHISHING_FOLDER

def handle_phishing_email(client, uid, subject, result):
    """
    Takes action on a phishing email: moves to quarantine folder, logs result.
    """
    print("🚨 Phishing email detected:")
    print(f"  ➤ Subject: {subject}")
    print(f"  ➤ Confidence: {result['confidence']:.2f}")

    try:
        # Create folder if it doesn't exist
        client.create_folder(PHISHING_FOLDER)
    except:
        pass  # Folder probably already exists

    # Move to phishing folder and mark as deleted in original
    client.copy(uid, PHISHING_FOLDER)
    client.delete_messages([uid])
    client.expunge()
    print("  ✅ Moved to quarantine folder.\n")

def handle_legitimate_email(subject, result):
    """
    Optionally log legitimate emails.
    """
    print("✅ Legitimate email:")
    print(f"  ➤ Subject: {subject}")
    print(f"  ➤ Confidence: {result['confidence']:.2f}\n")
