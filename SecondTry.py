import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Email details
sender_email = "examplemail@zohomail.eu"  # Your Zoho email address (authenticated)
receiver_email = "examplemail@insa-lyon.fr"      # Receiver's email address
forged_sender_email = "examplemailn@insa-lyon.fr"  # Forged sender's email address
subject = "Test Email from Zoho"
body = "This is a test email sent from Python using Zoho SMTP!"

# Zoho SMTP server details
smtp_server = "smtp.zoho.eu"
smtp_port = 587  # For TLS

# Set up the MIME message
message = MIMEMultipart()
message["From"] = f"Your dear dear friend (do not check the real mail) {forged_sender_email}"  # You cannot directly forge this in Zoho SMTP
message["To"] = receiver_email
message["Subject"] = subject
message["Reply-To"] = forged_sender_email  # Set the forged email address for replies
message.attach(MIMEText(body, "plain"))

# Zoho SMTP credentials
smtp_user = "examplemail@zohomail.eu"
smtp_password = "PASSWORD"  # Use an app-specific password if 2FA is enabled

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
