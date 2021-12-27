from flask import Flask
from flask_restful import Api
from flask_jwt_extended import JWTManager

from resources.table_game import TableGame, TableGameList
from resources.library import Library, LibraryList
from resources.user import UserRegister, UserLogin, UserLogout
from blocklist import JWT_BLOCKLIST


app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:password@172.17.28.198:5432/table_game_library'
app.config['JWT_SECRET_KEY'] = 'mykey'
api = Api(app)

@app.before_first_request
def create_tables():
    db.create_all() #only creates tables associated with sql alchemy

jwt = JWTManager(app)

@jwt.token_in_blocklist_loader
def check_if_token_is_revoked(jwt_header, jwt_payload):
    jti = jwt_payload['jti']
    return jti in JWT_BLOCKLIST

api.add_resource(TableGame, '/table-game/<int:id>') #/table-game/1
api.add_resource(TableGameList, '/table-games')
api.add_resource(Library, '/library/<string:name>')
api.add_resource(LibraryList, '/libraries')
#api.add_resource(User, '/user/<int:user_id>')
api.add_resource(UserRegister, '/register')
api.add_resource(UserLogin, '/login')
api.add_resource(UserLogout, '/logout')

if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(port=5000, debug=True)