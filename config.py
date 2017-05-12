import os

DEBUG = True
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

DATABASE_URI = os.path.join(BASE_DIR, "database.db")
SECRET_KEY = "secret"

# Mail settings

MAIL_SENDER = 'do-not-reply@example.com'
MAIL_DEBUG = True  # outputs email to console instead of sending them
