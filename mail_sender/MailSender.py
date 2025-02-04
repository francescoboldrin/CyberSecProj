import json
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from typing import re

from MailCrafter import craft_mail


# def convert_to_html(email_body, logo_cid):
#     """
#     Converts plain text email into HTML format with embedded links as buttons and a logo.
#     """
#     # Convert line breaks to HTML
#     email_body = email_body.replace("\n", "<br>")
#
#     # Convert links to HTML buttons
#     email_body = re.sub(r'\[(http[s]?:\/\/[^\]]+)\]',
#                         r'<br><a href="\1" style="display:inline-block;padding:10px 20px;color:#fff;background:#007bff;text-decoration:none;border-radius:5px;">Click Here</a><br>',
#                         email_body)
#
#     # Append logo at the bottom
#     email_body += f'<br><br><img src="cid:{logo_cid}" alt="Company Logo" style="width:150px; height:auto;">'
#
#     return f"""<html><body>{email_body}</body></html>"""

def send_mail(receiver):
    # Email details
    receiver_email = receiver["email"]  # The receiver's email address
    sender_email = "cybersecproj1@zohomail.eu"  # Your authenticated Zoho email address
    subject = "Login credentials retrieval"  # The subject of the email
    body = craft_mail(receiver)  # The body of the email

    # Zoho SMTP server details
    smtp_server = "smtp.zoho.eu"
    smtp_port = 587  # For TLS

    logo_path = "./mail_sender/images/zimbra-logo.png"  # Path to the logo image

    # Set up the MIME message
    message = MIMEMultipart()
    message["From"] = f"Login reinsert <{sender_email}>"  # Use authenticated email as 'From'
    message["To"] = receiver_email
    message["Subject"] = subject
    message["Reply-To"] = "dircom@insa-lyon.fr"  # Replies go to this address

    # Process email body
    logo_cid = "logo_cid"
    html_content = body
    message.attach(MIMEText(html_content, "html"))


    # Attach the logo image
    if os.path.exists(logo_path):
        with open(logo_path, "rb") as img:
            mime_image = MIMEImage(img.read(), name="zimbra-logo.png")
            mime_image.add_header("Content-ID", f"<{logo_cid}>")
            mime_image.add_header("Content-Disposition", "inline", filename="./images/zimbra-logo.png")
            message.attach(mime_image)
    else:
        print("⚠️ Logo file not found!")

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
    db_host = "./mail_sender/victims_data.json"  # Database host

    # Connect to the json database
    with open(db_host, "r") as file:
        data = json.load(file)

    return data
def sending_mails_to_victims():
    # Email details
    list_of_receivers = retrieve_emails_from_database()

    for receiver in list_of_receivers:
        if receiver["id"] == 0:
            send_mail(receiver)

sending_mails_to_victims()
