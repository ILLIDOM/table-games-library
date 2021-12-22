from flask_restful import Resource
from flask import request

from models.table_game_model import TableGameModel

# table game: (id, name, type, belongs_to, )

class TableGame(Resource):
    def get(self, id):
        table_game = TableGameModel.find_by_id(id)
        if table_game:
            return table_game.json(), 200
        else:
            return {'message': 'item not found'}, 404


    def post(self, id):
        if TableGameModel.find_by_id(id):
            return {'message': f"item with id {id} already exists"}, 400

        data = request.get_json() # throws error if empty or no valid json
        table_game = TableGameModel(data['name'], data['type'])

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

    def put(self, id):
        data = request.get_json()
        table_game = TableGameModel.find_by_id(id)

        if table_game is None:
            table_game = TableGameModel(data['name'], data['type'])
        else:
            table_game.name = data['name']
            table_game.type = data['type']

        table_game.save_to_db()
        return table_game.json(), 200