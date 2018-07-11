from e2e_cyber_utils.mysql_connector import MySqlConnection


def connect_to_clean_db():
    db_cnx = MySqlConnection(user='python_test_user',
                                  host='localhost',
                                  database='cyber_python_test_db',
                                  password='password')

    # Clear the tables
    for table in ['user', 'user_role_map', 'role']:
        db_cnx.execute_sql("TRUNCATE TABLE {}".format(table))

    # Insert the roles
    db_cnx.execute_sql("INSERT INTO role (role_name) VALUES ('ReadOnly'), ('Analyst'), ('Admin')")

    return db_cnx

