import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def send_email(subject: str, body: str, recipients: list[str]):
    """Send an email to a list of recipients using SMTP.

    Configuration is taken from environment variables:
        EMAIL_HOST: SMTP server host
        EMAIL_PORT: SMTP server port (optional, defaults to 587)
        EMAIL_USERNAME: username for login
        EMAIL_PASSWORD: password for login
        EMAIL_FROM: sender address
    """
    host = os.getenv("EMAIL_HOST")
    port = int(os.getenv("EMAIL_PORT", "587"))
    username = os.getenv("EMAIL_USERNAME")
    password = os.getenv("EMAIL_PASSWORD")
    sender = os.getenv("EMAIL_FROM")

    if not all([host, username, password, sender]):
        raise EnvironmentError("Missing required email configuration variables")

    message = MIMEMultipart()
    message["From"] = sender
    message["To"] = ", ".join(recipients)
    message["Subject"] = subject
    message.attach(MIMEText(body, "plain"))

    with smtplib.SMTP(host, port) as server:
        server.starttls()
        server.login(username, password)
        server.sendmail(sender, recipients, message.as_string())


if __name__ == "__main__":
    # Example usage
    recipients = ["example@example.com"]
    send_email(
        subject="Teste de envio",
        body="Mensagem de teste enviada automaticamente.",
        recipients=recipients,
    )
