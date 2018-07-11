import json
import unittest

import fakeredis
from hamcrest import *

import tests.test_api.test_utils
from cyber_python_test.user_api import api
from cyber_python_test.user_api.user_service import UserService


class TestUserEndpoint(unittest.TestCase):
    def setUp(self):
        api.e2e_cyber_api.app.testing = True
        api.e2e_cyber_api.allow_account_creation = True
        api.e2e_cyber_api.revoked_store = fakeredis.FakeStrictRedis()
        self.app = api.e2e_cyber_api.app.test_client()
        self.db_cnx = tests.test_api.test_utils.connect_to_clean_db()
        self.user_service = UserService(self.db_cnx)

    def test_get(self):
        self.user_service.save_user('endpoint.user', 'password')
        response = self.app.get('/users')

        assert_that(response.status_code, is_(200))

    def test_post(self):
        username = 'test.post'
        password = 'password'
        response = self.app.post('/users',
                                 data=json.dumps({'username': username, 'password': password}),
                                 content_type="application/json")

        assert_that(response.status_code, is_(200))
