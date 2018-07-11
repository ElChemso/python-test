### Python User Service and API Test

This test provides a single class called user_service and a single test class that tests it. 

The test is connected to a local instance of MySQL that contains three tables:
`user`, `role` and `user_role_map`. 

The `user` table contains: `id`, `username` and `password_hash`. 
The `role` table contains: `id` and `role_name`. 
The `user_role_map` contains `user_id` and `role_id`

At the start of each test the tables are all cleared and three roles inserted to the `role` table. 
The roles are: `ReadOnly`, `Analyst` and `Admin`. 

The method `get_results_as_dict` returns an AttrDict which allows the keys of the dictionary to be referenced 
via a . and the key name rather than square brackets, eg:
```python 
d = {'role': 'engineer'}
```
Can be accessed:
```python
d.role
```
or:
```python
d['role']
```
 
##### Objectives of the test:
1. Implement the missing methods and complete the unit test for `get_user_by_id`
2. Implement the missing method and unit test for `is_user_admin`
3. Fix the broken test `test_hash_password_returns_string`
4. Implement the missing method `authenticate_user`
5. Improve the security of the password hashing function

##### Secondary objectives
There is a users endpoint built on a flask. Using the user service finish this endpoint so it can create, and get users. 
