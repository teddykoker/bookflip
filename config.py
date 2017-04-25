DEBUG = True

import os
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

DATABASE_URI = os.path.join(BASE_DIR, "database.db")


SECRET_KEY = "secret"