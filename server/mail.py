
from . import app

host = app.config.get('MAIL_HOST', 'localhost')
username = app.config.get('MAIL_USERNAME')
password = app.config.get('MAIL_PASSWORD')
port = app.config.get('MAIL_PORT')
tls = app.config.get('MAIL_TLS', False)
ssl = app.config.get('MAIL_SSL', False)
debug = app.config.get('MAIL_DEBUG', False)
sender = app.config.get('MAIL_SENDER')
