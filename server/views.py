import sqlite3
import bcrypt

from flask import request, jsonify, session, abort

from server import app
from db import query_db


@app.route('/api/new', methods=['POST', 'GET'])
def new_listing():
    return str(request.get_json())


@app.route('/api/all')
def all_listings():
    listings = query_db('SELECT * FROM listings')
    return jsonify(listings)


@app.route('/api/users')
def all_users():
    users = query_db('SELECT * FROM users')
    return jsonify(users)


@app.route('/api/signup', methods=['POST'])
def signup():
    if (not request.json or 'email' not in request.json or
            'password' not in request.json or
            'username' not in request.json):
        abort(400)

    user = query_db('SELECT * FROM users WHERE email = ?',
                    (request.json['email'],), one=True)

    if user is not None:
        # report user already exists
        return ({'status': 'failed'})

    user = query_db('SELECT * FROM users WHERE username = ?',
                    (request.json['username'],), one=True)

    if user is not None:
        # report user already exists
        return ({'status': 'failed'})

    hashed = bcrypt.hashpw(request.json['password'].encode('utf-8'),
                           bcrypt.gensalt())

    query_db('INSERT INTO users (username,email,password) VALUES (?,?,?)',
             (request.json['username'], request.json['email'], hashed))

    # registration was successful
    return jsonify({'status': 'success'})


@app.route('/api/login', methods=['POST'])
def login():
    if (not request.json or 'username' not in request.json or
            'password' not in request.json):
        abort(400)

    print(request.json['username'] + " " + request.json['password'])

    user = query_db('SELECT * FROM users WHERE username = ?',
                    (request.json['username'],), one=True)

    if user is None:
        # report wrong email
        return jsonify({'status': 'failed'})

    if bcrypt.checkpw(request.json['password'].encode('utf-8'),
                      user['password'].encode('utf-8')):
        # login successful
        session["user_id"] = user["id"]
        return jsonify({'status': 'success'})

    # report wrong password
    return jsonify({'status': 'failed'})


@app.route('/api/logout')
def logout():
    session.pop('user_id', None)
    return jsonify({'status': 'success'})


@app.route('/api/me')
def me():
    if 'user_id' in session:
        return jsonify({'status': 'success'},
                       {'data': { 'authenticated': True}})
    return jsonify({'status': 'success'},
                   {'data': { 'authenticated': False}})


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    """
    Catch all that redirects to index.html for the single page application
    """
    return app.send_static_file('index.html')
