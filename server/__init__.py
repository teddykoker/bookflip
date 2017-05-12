from flask import Flask

app = Flask(__name__, instance_relative_config=True, static_url_path="")

# Load config from config.py
app.config.from_object('config')

# Load config from instance folder
app.config.from_pyfile('config.py')

import server.database
import server.views
