from flask import Flask, request
from flask_restful import Resource, Api
from flask_jwt import JWT, jwt_required

from security import authenticate, identity

app = Flask(__name__)
app.secret_key = 'mykey'
api = Api(app)
jwt = JWT(app, authenticate, identity) # creates new endpoint /auth

table_games = []

# table game: (id, name, type, belongs_to, )

class TableGame(Resource):
    @jwt_required()
    def get(self, id):
        table_game = next(filter(lambda x: x['id'] == id, table_games), None)
        return {'table-game': table_game}, 200 if table_game else 404

    def post(self, id):
        if next(filter(lambda x: x['id'] == id), None):
            return {'message': f"item with id {id} already exists"}, 400

        data = request.get_json() # throws error if empty or no valid json
        table_game = {'id': id, 'name': data['name'], 'type': data['type']}
        table_games.append(table_game)
        return table_game, 201

class Library(Resource):
    def get(self):
        return {'table-games': table_games}

api.add_resource(TableGame, '/table-games/<int:id>') #/table-game/1
api.add_resource(Library, '/library')

app.run(port=5000, debug=True)