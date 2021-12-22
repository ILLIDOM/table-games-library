from flask import Flask
from flask_restful import Api
from flask_jwt_extended import JWTManager, jwt_required, get_jwt_identity

from resources.table_game import TableGame

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.secret_key = 'mykey'
api = Api(app)
jwt = JWTManager(app)

api.add_resource(TableGame, '/table-games/<int:id>') #/table-game/1
#api.add_resource(Library, '/library')

if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(port=5000, debug=True)