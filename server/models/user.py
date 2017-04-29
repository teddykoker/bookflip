import bcrypt
from ..db import query_db


def all_users():
    return query_db('SELECT * FROM users')


def unique_email(email):
    user = query_db('SELECT * FROM users WHERE email = ?',
                    (email,), one=True)

    return user is None


def unique_username(username):
    user = query_db('SELECT * FROM users WHERE username = ?',
                    (username,), one=True)

    return user is None


def create_user(username, email, password):
    hashed = bcrypt.hashpw(password.encode('utf-8'),
                           bcrypt.gensalt())

    query_db('INSERT INTO users (username,email,password) VALUES (?,?,?)',
             (username, email, hashed))
