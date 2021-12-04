import sqlite3
from flask_restful import Resource, reqparse
from models.user import UserModel

class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("username",
        required=True,
        help="This cannot be blank.",
        type=str
    )
    parser.add_argument("password",
        required=True,
        help="This cannot be blank.",
        type=str
    )

    def post(self):
        data = UserRegister.parser.parse_args()

        if UserModel.find_by_username(data['username']):
            return {"message": "User already exist."}, 400
            
        user = UserModel(**data)
        user.save_to_db()

        return {"message": "User created sucessfully"}, 200
        

