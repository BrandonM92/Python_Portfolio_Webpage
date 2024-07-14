import smtplib
import ssl
import os
from dotenv import load_dotenv

load_dotenv()

def send_email(message, subject):
    host = "smtp.gmail.com"
    port = 465
    username = os.getenv("EMAIL")
    password = os.getenv("PASSWORD")
    receiver = os.getenv("EMAIL")

    # Create a secure SSL context
    context = ssl.create_default_context()

    # Format the email message with subject and body
    email_message = f"Subject: {subject}\r\n\r\n{message}"

    # Send the email
    with smtplib.SMTP_SSL(host=host, port=port, context=context) as server:
        server.login(user=username, password=password)
        server.sendmail(username, receiver, email_message)