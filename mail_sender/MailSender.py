import json
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from MailCrafter import craft_mail


def send_mail(receiver):
    # Email details
    receiver_email = receiver["email"]  # The receiver's email address
    sender_email = "cybersecproj1@zohomail.eu"  # Your authenticated Zoho email address
    subject = "Login credentials retrieval"  # The subject of the email
    body = craft_mail(receiver)  # The body of the email

    # Zoho SMTP server details
    smtp_server = "smtp.zoho.eu"
    smtp_port = 587  # For TLS

    # Set up the MIME message
    message = MIMEMultipart()
    message["From"] = f"Login reinsert <{sender_email}>"  # Use authenticated email as 'From'
    message["To"] = receiver_email
    message["Subject"] = subject
    message["Reply-To"] = "cybersecproj@zoho.mail.eu"  # Replies go to this address
    message.attach(MIMEText(body, "plain"))

    # Zoho SMTP credentials
    smtp_user = sender_email
    smtp_password = "Merlino.00"  # Use an app-specific password if 2FA is enabled

    # Establish connection to the SMTP server
    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()  # Start TLS encryption
            server.login(smtp_user, smtp_password)  # Log in to the SMTP server
            text = message.as_string()  # Convert the message to a string
            server.sendmail(sender_email, receiver_email, text)  # Send the email
            print("Email sent successfully!")
    except Exception as e:
        print(f"An error occurred: {e}")


def retrieve_emails_from_database():
    # Database connection details
    db_host = "./users_data.json"  # Database host

    # Connect to the json database
    with open(db_host, "r") as file:
        data = json.load(file)

    return data
def sending_mails_to_users():
    # Email details
    list_of_receivers = retrieve_emails_from_database()  # Retrieve emails from the database
    print(list_of_receivers)

    for receiver in list_of_receivers:
        send_mail(receiver)

sending_mails_to_users()