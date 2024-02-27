import smtplib
import re
import os

regex = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b"


def email_address_is_valid(email: str) -> bool:
    """
    Return True if email address format is valid, else False
    """
    if re.fullmatch(regex, email):
        return True
    else:
        return False


def send_email(to_email: str, subject: str, body: str) -> None:
    """
    Send a notification mail
    Raises:
        - ValueError if the email address is not in a valid format
        - ValueError if the smtp_username or the app_password is missing
        - SMTPAuthenticationError if authentication failed
    """
    if not email_address_is_valid(to_email):
        raise ValueError

    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    smtp_username = os.environ.get("SENDER_EMAIL_ADDRESS")
    app_password = os.environ.get("SMTP_APP_PASSWORD")

    if not smtp_username or not app_password:
        raise ValueError

    from_email = smtp_username
    to_email = to_email
    subject = "Hello, world!"
    body = "This is a test email."

    message = f"Subject: {subject}\n\n{body}"

    with smtplib.SMTP(smtp_server, smtp_port) as smtp:
        smtp.starttls()
        smtp.login(smtp_username, app_password)
        smtp.sendmail(from_email, to_email, message)
