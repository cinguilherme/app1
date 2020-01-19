import sqlite3
from flask_restful import Resource, reqparse
from models.user import User

parser = reqparse.RequestParser()
parser.add_argument('username', 
    type=str, required=True, help="this field cannot be blank")
parser.add_argument('password', 
    type=str, required=True, help="this field cannot be blank")


class UserResource(Resource):

    def get_data(self):
        return parser.parse_args()

    def post(self):
        data = self.get_data()
        
        if User.find_by_username(data['username']):
            return { 'message': 'username already exists' }, 400
        if User.create_new_user(data):
            return {'message': 'user created successfuly'}, 201


