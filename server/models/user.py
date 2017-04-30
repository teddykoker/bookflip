import bcrypt
from ..db import query_db


class User(object):
    def __init__(self, id):
        self._id = id

    @property
    def username(self):
        return query_db('SELECT username FROM users WHERE id = ?',
                        (self._id,), one=True)


    @property
    def email(self):
        return query_db('SELECT email FROM users WHERE id = ?',
                        (self._id,), one=True)


    @property
    def password(self):
        return query_db('SELECT password FROM users WHERE id = ?',
                        (self._id,), one=True)


    def check_password(self, password):
        return bcrypt.checkpw(password.encode('utf-8'),
                              self.password.encode('utf-8'))


    @staticmethod
    def all()
        ids = query_db('SELECT id FROM users')
        for user_id in ids:
            yield User(user_id)





class User(object):

    def __init__(self, username, email, password, id=None, saved=False):
        self.username = username
        self.email = email
        self.password = password
        self.saved = saved
        self.id = id


    def unique_email(self):
        user = query_db('SELECT * FROM users WHERE email = ?',
                        (self.email,), one=True)
        return user is None


    def unique_username(self):
        user = query_db('SELECT * FROM users WHERE username = ?',
                        (self.username,), one=True)
        return user is None


    def save(self):
        if not self.saved:
            query_db('INSERT INTO users (username,email,password) VALUES (?,?,?)',
                     (self.username, self.email, self.password))
            self = User.with_username(self.username)


    def check_password(self, password):
        return bcrypt.checkpw(password.encode('utf-8'),
                              self.password.encode('utf-8'))


    @staticmethod
    def hash_password(password):
        return bcrypt.hashpw(password.encode('utf-8'),
                             bcrypt.gensalt())


    @staticmethod
    def all():
        return query_db('SELECT * FROM users')


    @staticmethod
    def with_username(username):
        user = query_db('SELECT * FROM users WHERE username = ?',
                        (username,), one=True)

        if user is not None:
            return User(user['username'], user['email'], user['password'],
                        id=user['id'], saved=True)
        return None
