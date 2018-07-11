from cyber_python_test.user_api.endpoints.users import Users
from e2e_cyber_api import e2e_cyber_api
from e2e_cyber_api.e2e_cyber_api import app as application
from e2e_cyber_utils import mysql_connector

from cyber_python_test.user_api.user_service import UserService

db_cnx = mysql_connector.MySqlConnection(user='python_test_user',
                                         host='localhost',
                                         database='cyber_python_test_db',
                                         password='password')

user_service = UserService(db_cnx)

e2e_cyber_api.add_api()
e2e_cyber_api.api.add_resource(Users, "/users", "/users/<user_id>", resource_class_kwargs={"user_service": user_service})

if __name__ == "__main__":
    application.run()
