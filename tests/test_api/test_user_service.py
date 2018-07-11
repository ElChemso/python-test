import unittest

from hamcrest import *

import tests.test_api.test_utils
from cyber_python_test.user_api.user_service import UserService


class TestUserService(unittest.TestCase):

    def setUp(self):
        # This connects to the local MySQL instance and truncates the user, role and user_role_map tables
        self.db_cnx = tests.test_api.test_utils.connect_to_clean_db()

    def test_create_user(self):
        user_service = UserService(db_cnx=self.db_cnx)

        username = 'test.user'
        user_service.save_user(username, 'pw_hash')

        users = self.db_cnx.get_results_as_dict('SELECT * FROM user')

        assert_that(users.username, is_(username))

    def test_get_user(self):
        user_service = UserService(db_cnx=self.db_cnx)

        username = 'test.user'
        user_service.save_user(username, 'pw_hash')

        user = user_service.get_user_by_username(username)

        assert_that(user.username, is_(username))

    def test_assign_role_to_user(self):
        user_service = UserService(db_cnx=self.db_cnx)

        username = 'test.user'
        user_id = user_service.save_user(username, 'pw_hash')

        role_id = user_service.get_id_for_role('Analyst')

        user_service.assign_role_to_user(user_id, role_id)

        roles = user_service.get_roles_by_username(username)
        assert_that(roles, only_contains('Analyst'))

    def test_get_user_by_id(self):
        user_service = UserService(db_cnx=self.db_cnx)

        username = 'test.user'
        user_id = user_service.save_user(username, 'pw_hash')

        user = user_service.get_user_by_id(user_id)

        assert_that(user, is_not(None))

    def test_hash_password_returns_string(self):
        hashed_password = UserService(self.db_cnx).hash_password('test_password')

        assert_that(isinstance(hashed_password, str), is_(True))
