# email_fetcher.py

from imapclient import IMAPClient
from config import EMAIL_HOST, EMAIL_ADDRESS, EMAIL_PASSWORD, INBOX_FOLDER, MAX_EMAILS_PER_RUN

def connect_to_mailbox():
    """
    Connects to the IMAP email server and logs in.
    Returns: an active IMAPClient connection.
    """
    client = IMAPClient(EMAIL_HOST)
    client.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    client.select_folder(INBOX_FOLDER, readonly=False)
    return client

def fetch_unread_email_uids(client):
    """
    Fetches UIDs of unread emails in the INBOX.
    Returns: list of UIDs.
    """
    messages = client.search(["UNSEEN"])
    messages = messages[-MAX_EMAILS_PER_RUN:]  # Only process the most recent ones
    return messages

def fetch_email_message(client, uid):
    """
    Fetches the raw email message for a given UID.
    Returns: RFC822 email bytes.
    """
    response = client.fetch([uid], ["RFC822"])
    return response[uid][b"RFC822"]
