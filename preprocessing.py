# preprocessing.py

import re
from bs4 import BeautifulSoup

def clean_text(text: str) -> str:
    """
    Cleans the input email text by:
    - Stripping HTML tags
    - Lowercasing
    - Replacing URLs with 'urltoken'
    - Replacing numbers with 'numbertoken'
    - Removing special characters
    - Normalizing whitespace
    """
    if not isinstance(text, str):
        return ""

    # Strip HTML
    text = BeautifulSoup(text, "html.parser").get_text()

    # Lowercase
    text = text.lower()

    # Replace URLs
    text = re.sub(r'http\S+|www\S+|https\S+', ' urltoken ', text)

    # Replace numbers
    text = re.sub(r'\d+', ' numbertoken ', text)

    # Remove special characters
    text = re.sub(r'[^a-zA-Z\s]', '', text)

    # Collapse whitespace
    text = re.sub(r'\s+', ' ', text).strip()

    return text

def clean_subject_and_body(subject: str, body: str) -> str:
    """
    Cleans subject and body, combines them into a single string for model input.
    """
    subject_clean = clean_text(subject)
    body_clean = clean_text(body)
    return f"{subject_clean} {body_clean}"
