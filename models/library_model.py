from database import db

class LibraryModel(db.Model):
    __tablename__ = 'library'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    
    table_games = db.relationship('TableGameModel', lazy='dynamic') #lazy=dynamic; dont create relationship obj directly

    def __init__(self, name):
        self.name = name

    def json(self): #is slower with lazy=dynamic (each time a db access)
        return {
            'id': self.id,
            'name': self.name, 
            'table-games': [x.json() for x in self.table_games.all()]
            }

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first() #SELECT * FROM table_games WHERE name = name LIMIT 1

    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id=id).first()

    @classmethod
    def find_all(cls):
        return cls.query.all()

    def save_to_db(self): #update or insert
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()