import json

from flask import Response
from flask import request
from flask_restful import Resource


class Users(Resource):

    def __init__(self, user_service):
        self.user_service = user_service

    def get(self, user_id=None):
        """ This method should return a list of users or if a user id is specified a single user"""
        return Response(response=json.dumps(self.user_service.get_users()), status=200, mimetype="application/json")

    def post(self):
        username = request.json.get('username')
        password = request.json.get('password')
        roles = request.json.get('roles')
        """
        This method will take a username and password and create a user performing verification on the inputs
        :return:
        """
        pass

    def put(self, user_id):
        password = request.json.get('password')
        roles = request.json.get('password')
        """
        This method will allow a users password to be updated or new roles to be added depending on parameters passed
        :param user_id:
        :return:
        """
        pass
