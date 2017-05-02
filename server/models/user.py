from sqlalchemy import Column, Integer, String, Text, exists
from ..database import Base, db_session

import bcrypt


class User(Base):

    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(32), unique=True)
    email = Column(String(128), unique=True)
    password = Column(Text)

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = bcrypt.hashpw(password.encode('utf-8'),
                                      bcrypt.gensalt())

    def check_password(self, password):
        return bcrypt.checkpw(password.encode('utf-8'),
                              self.password.encode('utf-8'))

    def __repr__(self):
        return '<User %r>' % (self.name)

    @staticmethod
    def username_taken(username):
        return db_session.query(exists().where(User.username == username)).scalar()

    @staticmethod
    def email_taken(email):
        return db_session.query(exists().where(User.email == email)).scalar()
