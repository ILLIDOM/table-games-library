from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager

JWT_BLOCKLIST = set()

db = SQLAlchemy()
migrate = Migrate()
api = Api()
jwt = JWTManager()

'''FACTORY METHOD'''
# config can be object or string
def create_app(config='config.DevelopmentConfig'):
    app = Flask(__name__)
    app.config.from_object(config)

    with app.app_context():
        #Incldue API routes
        initialize_extensions(app)
        return app


def initialize_extensions(app):
    db.init_app(app)
    migrate.init_app(app, db)
    register_api(api) # api needs to be registered before api.init_app() is called

    # api call for testing if app is running
    # remove and make nicer
    @app.route('/', methods=['GET'])
    def home():
        return "APP is running"

    api.init_app(app)
    jwt.init_app(app)


def register_api(api):
    from core.resources.table_game import TableGame, TableGameList
    from core.resources.library import Library, LibraryList
    from core.resources.user import UserRegister, UserLogin, UserLogout

    api.add_resource(TableGame, '/table-game/<int:id>')
    api.add_resource(TableGameList, '/table-games')
    api.add_resource(Library, '/library/<int:id>')
    api.add_resource(LibraryList, '/libraries')
    api.add_resource(UserRegister, '/register')
    api.add_resource(UserLogin, '/login')
    api.add_resource(UserLogout, '/logout')


@jwt.token_in_blocklist_loader
def check_if_token_is_revoked(jwt_header, jwt_payload):
    jti = jwt_payload['jti']
    return jti in JWT_BLOCKLIST