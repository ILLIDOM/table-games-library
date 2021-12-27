from werkzeug.security import generate_password_hash, check_password_hash
from flask_restful import Resource
from flask import request
from flask_jwt_extended import (
    create_access_token,
    create_refresh_token,
    jwt_required,
    get_jwt
)

from models.user_model import UserModel
from blocklist import JWT_BLOCKLIST

# endpoint for user creation
class UserRegister(Resource):
    def post(self):
        data = request.get_json() # throws error if empty or no valid json
        if UserModel.find_by_username(data['username']):
            return {"message": "A user with that username already exists"}, 400
        password = generate_password_hash(data['password'])
        user = UserModel(data['username'], password)

        try:
            user.save_to_db()
        except:
            return {'message': 'error occured during insert'}, 500

        return {"message": "User created successfully."}, 201


class UserLogin(Resource):
    def post(self):
        data = request.get_json()
        user = UserModel.find_by_username(data['username'])

        #check password
        if user and check_password_hash(user.password, data['password']):
            # create access token
            access_token = create_access_token(identity=user.id, fresh=True)
            refresh_token = create_refresh_token(user.id)
            return {
                'access_token': access_token,
                'refresh_token': refresh_token
            }, 200

        return {'message': 'invalid credentials'}, 401 #unauthorized


class UserLogout(Resource):
    @jwt_required()
    def post(self):
        jti = get_jwt()['jti']
        JWT_BLOCKLIST.add(jti)
        return {'message': 'Successfully logged out'}, 200


# endpoint to manage user
# class User(Resource):
#     @classmethod
#     def get(cls, user_id):
#         user = UserModel.find_by_id(user_id)
#         if not user:
#             return {'message': 'user not found'}, 404
#         return user.json()

#     @classmethod
#     def delete(cls, user_id):
#         user = UserModel.find_by_id(user_id)
#         if not user:
#             return {'message': 'user not found'}, 404

#         user.delete_from_db()
#         return {'message': 'user deleted'}, 200