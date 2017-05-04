import sqlite3
import bcrypt

from flask import request, jsonify, session, abort

from server import app
from database import db_session

from models.user import User
from models.book import Book
from models.listing import Listing


@app.route('/api/all')
def all_listings():
    return jsonify([listing.serialized() for listing in Listing.query.all()])


@app.route('/api/users')
def all_users():
    return jsonify({})


@app.route('/api/signup', methods=['POST'])
def signup():
    if (not request.json or 'email' not in request.json or
            'password' not in request.json or
            'username' not in request.json):
        abort(400)

    if User.email_taken(request.json['email']):
        # report user with email already exists
        return jsonify({'status': 'failed'})

    if User.username_taken(request.json['username']):
        # report user with username already exists
        return jsonify({'status': 'failed'})

    # save user to database
    user = User(request.json['username'], request.json['email'],
                request.json['password'])

    db_session.add(user)
    db_session.commit()

    # registration was successful
    return jsonify({'status': 'success'})


@app.route('/api/login', methods=['POST'])
def login():
    if (not request.json or 'username' not in request.json or
            'password' not in request.json):
        abort(400)

    user = User.query.filter(User.username == request.json['username']).first()

    if user is None:
        # report wrong username
        return jsonify({'status': 'failed'})

    if user.check_password(request.json['password']):
        # login successful
        session["user_id"] = user.id
        return jsonify({'status': 'success'})

    # report wrong password
    return jsonify({'status': 'failed'})


@app.route('/api/logout')
def logout():
    session.pop('user_id', None)
    return jsonify({'status': 'success'})


@app.route('/api/new-listing', methods=['POST'])
def new_listing():

    book = Book.query.filter(
        Book.isbn == request.json['listing']['book']['isbn']).first()

    if book is None:
        book = Book(request.json['listing']['book']['isbn'],
                    request.json['listing']['book']['title'])
        db_session.add(book)
        db_session.commit()

    new_listing = Listing(request.json['listing']['price'])
    new_listing.book = book

    db_session.add(new_listing)
    db_session.commit()

    return jsonify({'status': 'success'})


@app.route('/api/me')
def me():
    if 'user_id' in session:
        return jsonify({'status': 'success', 'data': {'authenticated': True}})
    return jsonify({'status': 'success', 'data': {'authenticated': False}})


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    """
    Catch all that redirects to index.html for the single page application
    """
    return app.send_static_file('index.html')
