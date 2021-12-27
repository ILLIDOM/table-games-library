from flask_jwt_extended.utils import get_jwt_identity
from flask_restful import Resource
from flask import request
from flask_jwt_extended import jwt_required

from models.table_game_model import TableGameModel

class TableGame(Resource):
    @jwt_required()
    def get(self, id):
        table_game = TableGameModel.find_by_id(id)
        if table_game:
            return table_game.json(), 200
        else:
            return {'message': 'item not found'}, 404


    @jwt_required()
    def post(self, id):
        if TableGameModel.find_by_id(id):
            return {'message': f"item with id {id} already exists"}, 400

        data = request.get_json() # throws error if empty or no valid json
        # get user_id from jwt
        user_id = get_jwt_identity()
        table_game = TableGameModel(data['name'], data['type'], user_id, data['library_id'])

        try:
            table_game.save_to_db()
        except:
            return {'message': 'error occured during insert'}, 500

        return table_game.json(), 201


    def delete(self, id):
        table_game = TableGameModel.find_by_id(id)
        if table_game:
            table_game.delete_from_db()

        return {'message': 'item deleted'}, 200

    @jwt_required()
    def put(self, id):
        data = request.get_json()
        table_game = TableGameModel.find_by_id(id)
        user_id = get_jwt_identity()

        if table_game is None:
            table_game = TableGameModel(data['name'], data['type'], user_id, data['library_id'])
        else:
            table_game.name = data['name']
            table_game.type = data['type']
            table_game.library_id = data['library_id']

        table_game.save_to_db()
        return table_game.json(), 200


class TableGameList(Resource):
    @jwt_required()
    def get(self):
        user_id = get_jwt_identity()
        return {'table_games': [game.json() for game in TableGameModel.find_all_from_current_user(user_id)]}