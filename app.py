from flask import Flask
from flask_restful import Api
from flask_jwt_extended import JWTManager

from resources.table_game import TableGame, TableGameList
from resources.library import Library, LibraryList
from resources.user import User, UserRegister, UserLogin

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['JWT_SECRET_KEY'] = 'mykey'
api = Api(app)

@app.before_first_request
def create_tables():
    db.create_all() #only creates tables associated with sql alchemy

jwt = JWTManager(app)

api.add_resource(TableGame, '/table-game/<int:id>') #/table-game/1
api.add_resource(TableGameList, '/table-games')
api.add_resource(Library, '/library/<string:name>')
api.add_resource(LibraryList, '/libraries')
api.add_resource(User, '/user/<int:user_id>')
api.add_resource(UserRegister, '/register')
api.add_resource(UserLogin, '/login')

if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(port=5000, debug=True)