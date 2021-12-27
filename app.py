from flask import Flask
from flask_restful import Api
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager

from database import db # extra file for db because of circular dependencies
from resources.table_game import TableGame, TableGameList
from resources.library import Library, LibraryList
from resources.user import UserRegister, UserLogin, UserLogout
from blocklist import JWT_BLOCKLIST


app = Flask(__name__)
app.config.from_object('config.DevelopmentConfig')
api = Api(app)
migrate = Migrate(app, db)


@app.before_first_request
def create_tables():
    db.create_all() #only creates tables associated with sql alchemy

jwt = JWTManager(app)

@jwt.token_in_blocklist_loader
def check_if_token_is_revoked(jwt_header, jwt_payload):
    jti = jwt_payload['jti']
    return jti in JWT_BLOCKLIST

api.add_resource(TableGame, '/table-game/<int:id>')
api.add_resource(TableGameList, '/table-games')
api.add_resource(Library, '/library/<string:name>')
api.add_resource(LibraryList, '/libraries')
api.add_resource(UserRegister, '/register')
api.add_resource(UserLogin, '/login')
api.add_resource(UserLogout, '/logout')

if __name__ == '__main__':
    db.init_app(app)
    app.run(port=5000)