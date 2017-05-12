
import smtplib
from email.mime.text import MIMEText

from . import app

host = app.config.get('MAIL_HOST', 'localhost')
username = app.config.get('MAIL_USERNAME')
password = app.config.get('MAIL_PASSWORD')
port = app.config.get('MAIL_PORT')
tls = app.config.get('MAIL_TLS', False)
ssl = app.config.get('MAIL_SSL', False)
debug = app.config.get('MAIL_DEBUG', False)
sender = app.config.get('MAIL_SENDER')


def connect_server():
    server = None
    if sll:
        server = smtplib.SMTP_SSL(host, port)
    else:
        server = smtplib.SMTP(host, port)

    if tls:
        server.starttls()

    if username and password:
        server.login(username, password)

    return server


def send(message):
    if debug:
        print message.as_string()
    else:
        server = connect_server()
        server.sendmail(message.sender,
                        message.recipients,
                        message.as_string())


class Message(object):
    def __init__(self, subject='', recipients=[], body=None):

        self.recipients = recipients
        self.sender = sender

        msg = MIMEText(body)
        msg['Subject'] = subject
        msg['From'] = sender
        msg['To'] = ', '.join(recipients)

        self.msg = msg

    def as_string(self):
        return self.msg.as_string()
