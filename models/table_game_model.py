from database import db

class TableGameModel(db.Model):
    __tablename__ = 'table_game'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    type = db.Column(db.String(80))

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    #user = db.relationship('UserModel', back_populates='table_games')

    library_id = db.Column(db.Integer, db.ForeignKey('library.id'))
    #library = db.relationship('LibraryModel', back_populates='table_games')

    def __init__(self, name, type, user_id, library_id):
        self.name = name
        self.type = type
        self.user_id = user_id
        self.library_id = library_id

    def json(self):
        return {
            'id': self.id,
            'name': self.name, 
            'type': self.type,
            'user_id': self.user_id, 
            'library_id': self.library_id
            }

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first() #SELECT * FROM table_games WHERE name = name LIMIT 1

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()

    @classmethod
    def find_all(cls):
        return cls.query.all()

    @classmethod
    def find_all_from_current_user(cls, _id):
        return cls.query.filter_by(user_id=_id).all()

    def save_to_db(self): #update or insert
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()