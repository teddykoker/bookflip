import sqlite3
import bcrypt

from flask import request, jsonify

from server import app
from db import query_db


@app.route('/api/new', methods=['POST', 'GET'])
def new_listing():
  return str(request.get_json())


@app.route('/api/all')
def all_listings():
  listings = query_db('SELECT * FROM listings')
  return jsonify(listings)


@app.route('/api/register', methods=['POST'])
def register():
  if not request.json or not 'username' in request.json or not 'password' in request.json:
    abort(400)

  user = query_db('SELECT * FROM users WHERE username = ?',
                  request.json['username'], one=True)

  if user is not None:
    # TODO: report user already exists
    return ""

  hashed = bcrypt.hashpw(password, bcrypt.gensalt())

  query_db('INSERT INTO users (username,password) VALUES (?,?)',
           (request.json['username'], hashed))

  # TODO: return okay
  return ""

@app.route('/api/login', methods=['POST'])
def login():
  if not request.json or not 'username' in request.json or not 'password' in request.json:
    abort(400)


  user = query_db('SELECT * FROM users WHERE username = ?',
                  request.json['username'], one=True)

  if user is None:
    # TODO: report wrong username
    return ""

  if bcrypt.checkpw(request.json['password'], user['password']):
    # TODO: login successful request stuff
    return ""


@app.route('/me')
def me():
  return ""


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
  """
  Catch all that redirects to index.html for the single page application
  """
  return app.send_static_file('index.html')