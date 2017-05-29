import os
import server
import unittest
import tempfile
import json

from server.models import db, User

class TestConfig:
    SERVER_NAME = 'localhost:5000'

    DEBUG = True
    TESTING = True
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))

    SQLALCHEMY_DATABASE_URI = 'sqlite://'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    SECRET_KEY = "secret"

    # Mail settings

    MAIL_SENDER = 'do-not-reply@example.com'
    MAIL_DEBUG = True  # outputs email to console instead of sending them

class ServerTestCase(unittest.TestCase):

    def setUp(self):

        self.app = server.create_app(TestConfig)

        self.app_context = self.app.app_context()
        self.app_context.push()

        db.create_all()

        self.test_user = User('test', 'test@example.com', 'password')
        db.session.add(self.test_user)
        db.session.commit()

        self.client = self.app.test_client()

    def tearDown(self):
        db.drop_all()
        db.session.remove()
        self.app_context.pop()


    def test_not_authenticated(self):
        # check authentication status
        response = self.client.get('/api/me')
        assert json.loads(response.data.decode('utf-8')) == {'status': 'success',
                                             'data': {'authenticated': False}}

        # try to create new listing while unauthenticated
        response = self.client.post('/api/listings')
        assert response.status_code == 401

    def test_signup(self):
        data = json.dumps(dict(username='signup',
                               password='password',
                               email='signup@example.com'))
        response = self.client.post('/api/signup',
                                    data=data,
                                    content_type='application/json')
        assert 'success' in response.data.decode('utf-8')

    def test_activate_user(self):
        self.client.get(self.test_user.activation_link)

        assert self.test_user.active == True

    def test_login(self):
        # post credentials to login
        data = json.dumps(dict(username='test',
                               password='password'))
        response = self.client.post('/api/login',
                                    data=data,
                                    content_type='application/json')
        assert 'success' in response.data.decode('utf-8')

        # check athentication status
        response = self.client.get('/api/me')
        assert json.loads(response.data.decode('utf-8')) == {'status': 'success',
                                             'data': {'authenticated': True}}


    def test_all_listings(self):
        response = self.client.get('/api/listings')
        assert 'success' in response.data.decode('utf-8')


    def test_new_listing(self):

        with self.client.session_transaction() as session:
            # authenticate user
            session['user_id'] = self.test_user.id

        data = json.dumps(dict(listing=dict(book=dict(title='BookTitle',
                                                      isbn=1111111111111),
                                            price=123)))
        response = self.client.post('/api/listings',
                                    data=data,
                                    content_type='application/json')
        assert 'success' in response.data.decode('utf-8')




if __name__ == '__main__':
    unittest.main()
