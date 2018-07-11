import hashlib


class UserService(object):
    def __init__(self, db_cnx):
        self.db_cnx = db_cnx

    @staticmethod
    def hash_password(password):
        return hashlib.md5(password.encode())

    def save_user(self, username, password):
        password_hash = self.hash_password(password)
        return self.db_cnx.execute_sql("INSERT INTO user (username, password_hash) "
                                       "VALUES ('{username}', '{hash}')".format(username=username,
                                                                                hash=password_hash))

    def get_user_by_username(self, username):
        return self.db_cnx.get_results_as_dict("SELECT * FROM user where username = '{username}'".format(username=username))

    def assign_role_to_user(self, user_id, role_id):
        self.db_cnx.execute_sql("INSERT INTO user_role_map VALUES ({user_id}, {role_id})".format(user_id=user_id, role_id=role_id))

    def get_id_for_role(self, role):
        return self.db_cnx.get_results_as_dict("SELECT id FROM role where role_name = '{}'".format(role)).id

    def get_roles_by_username(self, username):
        roles = self.db_cnx.get_results_as_dict("SELECT role_name FROM role "
                                                "LEFT JOIN user_role_map urm ON urm.role_id = role.id "
                                                "LEFT JOIN user ON user.id = urm.user_id "
                                                "WHERE user.username = '{username}'".format(username=username), force_list=True)
        return [r.role_name for r in roles]

    def get_users(self):
        return self.db_cnx.get_results_as_dict("SELECT * FROM user")

    def get_user_by_id(self, user_id):
        # TODO: This should return the user with the given ID
        pass

    def is_user_admin(self, username):
        # TODO: This should return true if the user has the admin role
        pass

    def authenticate_user(self, username, password):
        # TODO: This should return a boolean if the correct password has been provided for the user
        pass
