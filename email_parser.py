# email_parser.py

import email
from email.header import decode_header

def extract_email_content(raw_email_bytes):
    """
    Takes raw RFC822 email bytes and returns subject and plain-text body.
    Returns: (subject: str, body: str)
    """
    try:
        # Parse the raw message
        msg = email.message_from_bytes(raw_email_bytes)

        # --- Decode Subject ---
        raw_subject = msg["Subject"]
        if raw_subject:
            decoded_parts = decode_header(raw_subject)
            subject = ''
            for part, encoding in decoded_parts:
                if isinstance(part, bytes):
                    subject += part.decode(encoding or "utf-8", errors="ignore")
                else:
                    subject += part
        else:
            subject = ""

        # --- Extract Body ---
        body = ""
        if msg.is_multipart():
            for part in msg.walk():
                content_type = part.get_content_type()
                content_disposition = str(part.get("Content-Disposition"))

                if content_type == "text/plain" and "attachment" not in content_disposition:
                    try:
                        body = part.get_payload(decode=True).decode(part.get_content_charset() or "utf-8", errors="ignore")
                        break
                    except:
                        continue
        else:
            try:
                body = msg.get_payload(decode=True).decode(msg.get_content_charset() or "utf-8", errors="ignore")
            except:
                body = ""

        return subject.strip(), body.strip()

    except Exception as e:
        print(f"⚠️ Failed to parse email: {e}")
        return "", ""
