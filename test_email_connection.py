# test_email_connection.py

from imapclient import IMAPClient
from config import EMAIL_HOST, EMAIL_ADDRESS, EMAIL_PASSWORD, INBOX_FOLDER

def test_connection():
    try:
        print(f"Connecting to {EMAIL_HOST}...")
        with IMAPClient(EMAIL_HOST) as client:
            client.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            print("✅ Login successful.")

            client.select_folder(INBOX_FOLDER, readonly=True)
            num_messages = len(client.search(["ALL"]))
            print(f"📥 INBOX contains {num_messages} messages.")

    except Exception as e:
        print(f"❌ Connection failed: {e}")

if __name__ == "__main__":
    test_connection()
