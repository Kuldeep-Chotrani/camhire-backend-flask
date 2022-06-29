import sqlite3

from flask_restful import Resource, reqparse

from models.user import UserModel


class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        'username',
        type=str,
        required=True
    )
    parser.add_argument(
        'password',
        type=str,
        required=True
    )
    def post(self):

        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        data = UserRegister.parser.parse_args()
        insert_user = "INSERT INTO users VALUES(NULL,?,?)"
        if UserModel.find_by_username(data['username']):
            message = "Already exist"
        else:
            user = UserModel(**data)
            user.save_to_db()
            message = "User created"
        return {"Messgage": message}, 201