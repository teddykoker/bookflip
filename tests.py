import os
import server
import unittest
import tempfile
import json

class TestConfig(object):
    DEBUG = True
    TESTING = True
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))

    DATABASE_URI = os.path.join(BASE_DIR, "test.db")
    SECRET_KEY = "secret"

    # Mail settings

    MAIL_SENDER = 'do-not-reply@example.com'
    MAIL_DEBUG = True  # outputs email to console instead of sending them

class ServerTestCase(unittest.TestCase):

    def setUp(self):

        self.app = server.create_app(TestConfig)

        #with self.app.app_context():
        server.database.db.create_all()


        self.client = self.app.test_client()

    def tearDown(self):
        server.database.db.drop_all()
        server.database.db.session.remove()


    def test_not_authenticated(self):
        response = self.client.get('/api/me')
        assert json.loads(response.data) == {'status': 'success',
                                       'data': {'authenticated': False}}

    def test_signup(self):
        for user in server.models.user.User.query.all():
            print user

        data = json.dumps(dict(username='test3',
                               password='test',
                               email='test3@test.com'))

        response = self.client.post('/api/signup',
                                 data=data,
                                 content_type='application/json')
        print(response.data)
        assert 'success' in response.data


    def test_a(self):
        assert True

    def test_b(self):
        assert True

if __name__ == '__main__':
    unittest.main()
