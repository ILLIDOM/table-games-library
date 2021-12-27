from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager

from application.blocklist import JWT_BLOCKLIST

db = SQLAlchemy()
migrate = Migrate()
api = Api()
jwt = JWTManager()


def create_app():
    '''Initalize core application'''
    app = Flask(__name__)
    app.config.from_object('config.DevelopmentConfig')

    with app.app_context():
        #Incldue API routes
        initialize_extensions(app)
        return app


def initialize_extensions(app):
    db.init_app(app)
    migrate.init_app(app, db)
    initialize_api(api)
    api.init_app(app)
    jwt.init_app(app)


def initialize_api(api):
    from application.resources.table_game import TableGame, TableGameList
    from application.resources.library import Library, LibraryList
    from application.resources.user import UserRegister, UserLogin, UserLogout

    api.add_resource(TableGame, '/table-game/<int:id>')
    api.add_resource(TableGameList, '/table-games')
    api.add_resource(Library, '/library/<string:name>')
    api.add_resource(LibraryList, '/libraries')
    api.add_resource(UserRegister, '/register')
    api.add_resource(UserLogin, '/login')
    api.add_resource(UserLogout, '/logout')


@jwt.token_in_blocklist_loader
def check_if_token_is_revoked(jwt_header, jwt_payload):
    jti = jwt_payload['jti']
    return jti in JWT_BLOCKLIST