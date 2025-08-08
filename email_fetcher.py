# email_fetcher.py

from imapclient import IMAPClient
from config_loader import load_config
config = load_config()

def connect_to_mailbox():
    """
    Connects to the IMAP email server and logs in.
    Returns: an active IMAPClient connection.
    """
    client = IMAPClient(config.EMAIL_HOST)
    client.login(config.EMAIL_ADDRESS, config.EMAIL_PASSWORD)
    client.select_folder(config.INBOX_FOLDER, readonly=False)
    return client

def fetch_unread_email_uids(client):
    """
    Fetches UIDs of unread emails in the INBOX.
    Returns: list of UIDs.
    """
    messages = client.search(["UNSEEN"])
    messages = messages[-config.MAX_EMAILS_PER_RUN:]  # Only process the most recent ones
    return messages

def fetch_email_message(client, uid):
    """
    Fetches the raw email message for a given UID.
    Returns: RFC822 email bytes.
    """
    response = client.fetch([uid], ["RFC822"])
    return response[uid][b"RFC822"]
