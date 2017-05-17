import sqlite3
import bcrypt

from flask import Blueprint, request, jsonify, session, abort, url_for, current_app
from itsdangerous import URLSafeSerializer, BadSignature

from ..database import db

from ..utils import api_response

from ..mail import mail, Message

from ..models.user import User
from ..models.book import Book
from ..models.listing import Listing

api = Blueprint('api', __name__)


@api.route('/all')
def all_listings():

    listings = [listing.serialized() for listing in Listing.query.all()]
    return api_response('success', {'listings': listings})


@api.route('/users')
def all_users():
    return api_response('success', {})


@api.route('/signup', methods=['POST'])
def signup():
    if (not request.json or 'email' not in request.json or
            'password' not in request.json or
            'username' not in request.json):
        abort(400)

    if User.email_taken(request.json['email']):
        # report user with email already exists
        return api_response('failed', 'email exists')

    if User.username_taken(request.json['username']):
        # report user with username already exists
        return api_response('failed', 'username exists')

    # save user to database
    user = User(request.json['username'], request.json['email'],
                request.json['password'])

    db.session.add(user)
    db.session.commit()

    print("click this link: " + get_activation_link(user) + " to activate")

    # registration was successful
    return api_response('success')


@api.route('/login', methods=['POST'])
def login():
    if (not request.json or 'username' not in request.json or
            'password' not in request.json):
        abort(400)

    user = User.query.filter(User.username == request.json['username']).first()

    if user is None:
        # report wrong username
        return api_response('failed')

    if user.check_password(request.json['password']):
        # login successful
        session["user_id"] = user.id
        return api_response('success')

    # report wrong password
    return api_response('failed')


@api.route('/logout')
def logout():
    session.pop('user_id', None)
    return jsonify({'status': 'success'})


@api.route('/new-listing', methods=['POST'])
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

    return api_response('success')


@api.route('/me')
def me():
    if 'user_id' in session:
        return api_response('success', {'authenticated': True})
    return api_response('success', {'authenticated': False})


# @api.route('/test-mail')
# def test_mail():
#     msg = Message(subject='test subject',
#                        recipients=['recipient@example.com'],
#                        body='body content')

#     mail.send(msg)
#     return 'sent message'

def get_serializer(secret_key=None):
    if secret_key is None:
        secret_key = current_app.secret_key
    return URLSafeSerializer(secret_key)


def get_activation_link(user):
    s = get_serializer()
    payload = s.dumps(user.id)
    return url_for('activate_user', payload=payload, _external=True)


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