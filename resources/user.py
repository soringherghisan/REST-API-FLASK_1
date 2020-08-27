"""
- User class

    - rather than using a dict, he chose to store info in an Obj.
"""

import sqlite3
from flask_restful import Resource, reqparse

from models.UserModel import UserModel


# resource we use to sign up
class UserRegister(Resource):
    # reqparse
    parser = reqparse.RequestParser()
    parser.add_argument('username', type=str, required=True, help='YOU FORGOT THE usenrmae')
    parser.add_argument('password', type=str, required=True, help='YOU FORGOT THE password')

    def post(self):
        data = UserRegister.parser.parse_args()

        # check if username already exists
        if UserModel.find_by_username(username=data['username']):
            return {'messagio': 'ALREADU EXOSTS !'}, 400  # 201 - response code - created

        user = UserModel(**data)  # unpacking with **
        user.save_to_db()

        return {'messagio': 'User was created succesfuly !'}, 201  # 201 - response code - created
