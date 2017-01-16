import time
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from config import SMTP_PORT, SMTP_HOST, SMTP_PROTOCOL, EMAIL_LOGIN, EMAIL_PASSWORD


def current_date():
    """Get current date in format dd/mm/yyy"""
    return time.strftime("%d/%m/%Y")


def file_to_text(file, encoding="utf-8"):
    """Attach text file on email"""
    try:
        with open(file, "r", encoding=encoding) as file:
            return "".join(file.read())
    except FileNotFoundError:
        return "File not found!"


def send_mail_smtp(subject, body, mail_to, protocol=SMTP_PROTOCOL):
    """Send email by smtp"""
    if protocol == "SSL":
        server = smtplib.SMTP_SSL()
        server.connect(SMTP_HOST, SMTP_PORT)
        server.ehlo()
    else:
        server = smtplib.SMTP()
        server.connect(SMTP_HOST, SMTP_PORT)
        server.ehlo()
        server.starttls()
        server.ehlo()
    server.login(EMAIL_LOGIN, EMAIL_PASSWORD)
    # Configure body message
    msg = MIMEMultipart()
    msg["From"] = EMAIL_LOGIN
    msg["To"] = mail_to
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "plain"))
    # Send email
    server.send_message(msg, EMAIL_LOGIN, mail_to)
    server.quit()
    return "Email was sent to {mail}".format(mail=mail_to)
