# main.py

from email_fetcher import connect_to_mailbox, fetch_unread_email_uids, fetch_email_message
from email_parser import extract_email_content
from phishing_classifier import PhishingEmailClassifier
from action_handler import handle_phishing_email, handle_legitimate_email

def main():
    print("📡 Starting phishing email scanner...")

    # Step 1: Connect to email inbox
    try:
        client = connect_to_mailbox()
        print("✅ Connected to email server.")
    except Exception as e:
        print(f"❌ Failed to connect to mailbox: {e}")
        return

    # Step 2: Fetch unread email UIDs
    uids = fetch_unread_email_uids(client)
    if not uids:
        print("📭 No unread emails to process.")
        return
    print(f"📨 Found {len(uids)} unread email(s).")

    # Step 3: Load classifier
    classifier = PhishingEmailClassifier()

    # Step 4: Process each email
    for uid in uids:
        raw_email = fetch_email_message(client, uid)
        subject, body = extract_email_content(raw_email)

        if not subject and not body:
            print(f"⚠️ Skipping empty or unparsable email UID: {uid}")
            continue

        result = classifier.predict(subject, body)

        if result["label"] == "phishing":
            handle_phishing_email(client, uid, subject, result)
        else:
            handle_legitimate_email(subject, result)

    print("✅ Done scanning.")

if __name__ == "__main__":
    main()
