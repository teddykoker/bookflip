import sqlite3
import bcrypt

from flask import Blueprint, request, jsonify, session, abort, url_for, current_app
from itsdangerous import URLSafeSerializer, BadSignature

from ..mail import mail, Message
from ..models import db, User, Listing, Book
from ..decorators import jsonapi
from ..utils import get_serializer

api = Blueprint('api', __name__)


@api.route('/listings', methods=['GET'])
@jsonapi
def all_listings():

    listings = [listing.serialized() for listing in Listing.query.all()]
    return 'success', {'listings': listings}


@api.route('/users')
@jsonapi
def all_users():
    return 'success', {}


@api.route('/signup', methods=['POST'])
@jsonapi
def signup():
    if (not request.json or 'email' not in request.json or
            'password' not in request.json or
            'username' not in request.json):
        abort(400)

    if User.email_taken(request.json['email']):
        # report user with email already exists
        return 'failed', 'email exists'

    if User.username_taken(request.json['username']):
        # report user with username already exists
        return 'failed', 'username exists'

    # save user to database
    user = User(request.json['username'], request.json['email'],
                request.json['password'])

    db.session.add(user)
    db.session.commit()

    print("click this link: " + user.activation_link + " to activate")

    # registration was successful
    return 'success', {}


@api.route('/login', methods=['POST'])
@jsonapi
def login():
    if (not request.json or 'username' not in request.json or
            'password' not in request.json):
        abort(400)

    user = User.query.filter(User.username == request.json['username']).first()

    if user is None:
        # report wrong username
        return 'failed', {}

    if user.check_password(request.json['password']):
        # login successful
        session["user_id"] = user.id
        return 'success', {}

    # report wrong password
    return 'failed', {}


@api.route('/logout')
@jsonapi
def logout():
    session.pop('user_id', None)
    return 'success', {}


@api.route('/listings', methods=['POST'])
@jsonapi
def new_listing():

    book = Book.query.filter(
        Book.isbn == request.json['listing']['book']['isbn']).first()

    if book is None:
        book = Book(request.json['listing']['book']['isbn'],
                    request.json['listing']['book']['title'])
        db.session.add(book)
        db.session.commit()

    new_listing = Listing(request.json['listing']['price'])
    new_listing.book = book

    db.session.add(new_listing)
    db.session.commit()

    return 'success', {}


@api.route('/me')
@jsonapi
def me():
    if 'user_id' in session:
        return 'success', {'authenticated': True}
    return 'success', {'authenticated': False}

# @api.route('/test-mail')
# def test_mail():
#     msg = Message(subject='test subject',
#                        recipients=['recipient@example.com'],
#                        body='body content')

#     mail.send(msg)
#     return 'sent message'

@api.route('/activate/<payload>')
def activate_user(payload):
    s = get_serializer()
    try:
        user_id = s.loads(payload)
    except BadSignature:
        abort(400)

    user = User.query.filter(User.id == user_id).first()
    if user is not None:
        user.activate()
    else:
        abort(400)

    return "user activated"





#from . import users, listings, books
