import smtplib
from email.mime.text import MIMEText
from config import load_config
from utils import log_message

def send_alert(message):
    config = load_config()
    msg = MIMEText(message)
    msg['Subject'] = 'Server Alert'
    msg['From'] = config['email_from']
    msg['To'] = config['email_to']

    try:
        with smtplib.SMTP(config['smtp_server'], config['smtp_port']) as server:
            server.login(config['smtp_user'], config['smtp_password'])
            server.sendmail(config['email_from'], [config['email_to']], msg.as_string())
        log_message(f"Alert sent: {message}")
    except Exception as e:
        log_message(f"Failed to send alert: {e}", 'error')