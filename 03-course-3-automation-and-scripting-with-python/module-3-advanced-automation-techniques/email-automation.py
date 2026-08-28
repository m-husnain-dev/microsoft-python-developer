import imaplib
import smtplib
from email.mime.text import MIMEText

# Setup for email connection
smtp_server = "smtp.example.com"
smtp_port = 587
imap_server = "imap.example.com"
imap_port = 993
email_user = "orders@example.com"
email_password = "Coursera1000!"


def send_confirmation_email(client_email, client_name):
    message = MIMEText(f"Thank you for your order, {client_name}!")
    message['Subject'] = "Order Confirmation"
    message['From'] = email_user
    message['To'] = client_email

    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(email_user, email_password)
        server.send_message(message)

    print(f"Sent confirmation email to {client_name}!")


def check_new_messages(client_email, client_name):
    with imaplib.IMAP4_SSL(imap_server, imap_port) as mail:
        mail.login(email_user, email_password)
        mail.select('inbox')

        status, responses = mail.search(
            None, '(UNSEEN FROM "%s")' % client_email
        )

        if responses[0]:
            print(f"New message from {client_name}!")
        else:
            print("No new messages yet.")


# Example usage
client_email = "john.smith@example.com"
client_name = "John Smith"

send_confirmation_email(client_email, client_name)
check_new_messages(client_email, client_name)