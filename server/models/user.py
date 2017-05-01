import bcrypt
from ..db import query_db


class User(object):
    def __init__(self, id):
        self._id = id

    @property
    def id(self):
        return self._id

    @property
    def username(self):
        return query_db('SELECT username FROM users WHERE id = ?',
                        (self._id,), one=True)['username']


    @property
    def email(self):
        return query_db('SELECT email FROM users WHERE id = ?',
                        (self._id,), one=True)['email']


    @property
    def password(self):
        return query_db('SELECT password FROM users WHERE id = ?',
                        (self._id,), one=True)['password']


    def check_password(self, password):
        return bcrypt.checkpw(password.encode('utf-8'),
                              self.password.encode('utf-8'))


    @staticmethod
    def all():
        users = query_db('SELECT id FROM users')
        for user in users:
            yield User(user['id'])


    @staticmethod
    def add(username, email, password):
        query_db('INSERT INTO users (username,email,password) VALUES (?,?,?)',
                 (username, email, password))


    @staticmethod
    def with_username(username):
        user = query_db('SELECT id FROM users WHERE username = ?',
                      (username,), one=True)
        if user is not None:
            return User(user['id'])
        return None


    @staticmethod
    def with_email(email):
        id = query_db('SELECT id FROM users WHERE email = ?',
                      (email,), one=True)
        if id is not None:
            return User(id)
        return None


    @staticmethod
    def hash_password(password):
        return bcrypt.hashpw(password.encode('utf-8'),
                             bcrypt.gensalt())
