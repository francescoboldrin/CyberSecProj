import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

import socket

def check_smtp_connection(smtp_server, smtp_port):
    try:
        # Try to create a socket connection to the SMTP server
        with socket.create_connection((smtp_server, smtp_port), timeout=10) as s:
            # find the connection metadata
            print(s)

            print(f"Successfully connected to {smtp_server} on port {smtp_port}")
    except socket.error as e:
        print(f"Failed to connect to {smtp_server} on port {smtp_port}. Error: {e}")

# Replace with your actual SMTP server and port
smtp_server = "smtp.insa-lyon.fr"  # Example SMTP server
smtp_port = 587  # Port for STARTTLS (or 465 for SSL)

# Check the connection
check_smtp_connection(smtp_server, smtp_port)



import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import logging


# def check_auth_methods():
#     smtp_server = "smtp.insa-lyon.fr"
#     smtp_port = 587  # or 465 for SSL
#     try:
#         with smtplib.SMTP(smtp_server, smtp_port) as server:
#             server.set_debuglevel(1)  # Enable debug output for SMTP connection
#             server.helo()  # Initial connection
#             response = server.docmd('EHLO', 'example.com')  # Get available extensions
#             print(response)  # This will print the available server extensions
#     except Exception as e:
#         print(f"An error occurred: {e}")
#
# check_auth_methods()

# exit()

def send_email():
    smtp_server = "smtp.insa-lyon.fr"
    smtp_port = 587  # Port for STARTTLS
    smtp_user = "examplemail@insa-lyon.fr"  # Your email address
    smtp_password = "PASSWORD"  # Your password (or app-specific password)
    sender_email = "examplemail@insa-lyon.fr"  # Your email address
    receiver_email = "examplemail@insa-lyon.fr"  # Receiver's email address
    subject = "Test Email from INSA Lyon"
    body = "This is a test email sent without SMTP AUTH."

    # Set up the MIME message
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject
    message.attach(MIMEText(body, "plain"))

    logging.basicConfig(level=logging.DEBUG)

    try:

        # Create an SSL context to specify SSL version compatibility
        context = ssl.create_default_context()
        context.set_ciphers('TLSv1.2')  # Force use of TLSv1.2 for compatibility

        print("trying to connect to the server")

        # Establish a connection using SSL (on port 465)
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            print("Successfully connected to the server: ", server)

            # logging.debug("Successfully connected to the server: ", server)
            server.set_debuglevel(1)

            server.starttls(context=context)  # Secure the connection

            server.ehlo()  # Identify yourself to the server

            # # Login with credentials
            # server.login(smtp_user, smtp_password)  # Login with credentials
            # print("Successfully authenticated and connected to the server.")

            # Send the email
            text = message.as_string()  # Convert message to string format
            server.sendmail(sender_email, receiver_email, text)
            print("Email sent successfully!")
    except smtplib.SMTPException as e:
        print(f"An error occurred: {e}")


# Send the email
send_email()

# # Email details
# sender_email = "examplemail@insa-lyon.fr"  # Your email address with the domain
# receiver_email = "examplemail@gmail.com"          # Receiver's email address
# subject = "Test Email from INSA Lyon"
# body = "This is a test email sent from Python using the INSA Lyon SMTP server!"
#
# # INSA Lyon SMTP server details (replace with the actual server and port)
# smtp_server = "smtp.insa-lyon.fr"  # Replace with actual SMTP server
# smtp_port = 587  # Typically, 587 is used for TLS
#
# # Set up the MIME message
# message = MIMEMultipart()
# message["From"] = sender_email
# message["To"] = receiver_email
# message["Subject"] = subject
# message.attach(MIMEText(body, "plain"))
#
# # INSA Lyon SMTP credentials (replace with your actual credentials)
# smtp_user = "examplemail@insa-lyon.fr"  # Your INSA Lyon email address
# smtp_password = "PASSWORD"  # Your password (or app-specific password)
#
# # Establish connection to the SMTP server
# try:
#     with smtplib.SMTP(smtp_server, smtp_port) as server:
#         server.starttls()  # Start TLS encryption
#         server.login(smtp_user, smtp_password)  # Log in to the SMTP server
#         text = message.as_string()  # Convert the message to a string
#         server.sendmail(sender_email, receiver_email, text)  # Send the email
#         print("Email sent successfully!")
# except Exception as e:
#     print(f"An error occurred: {e}")
