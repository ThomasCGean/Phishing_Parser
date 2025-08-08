# test_email_connection.py

from imapclient import IMAPClient
from config_loader import load_config
config = load_config()

def test_connection():
    try:
        print(f"Connecting to {config.EMAIL_HOST}...")
        with IMAPClient(config.EMAIL_HOST) as client:
            client.login(config.EMAIL_ADDRESS, config.EMAIL_PASSWORD)
            print("✅ Login successful.")

            client.select_folder(config.INBOX_FOLDER, readonly=True)
            num_messages = len(client.search(["ALL"]))
            print(f"📥 INBOX contains {num_messages} messages.")

    except Exception as e:
        print(f"❌ Connection failed: {e}")

if __name__ == "__main__":
    test_connection()
