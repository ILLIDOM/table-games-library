from db import db

class TableGameModel(db.Model):
    __tablename__ = 'table_games'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    type = db.Column(db.String(80))

    def __init__(self, name, type):
        self.name = name
        self.type = type

    def json(self):
        return {'name': self.name, 'type': self.type}

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first() #SELECT * FROM table_games WHERE name = name LIMIT 1

    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id=id).first()

    def save_to_db(self): #update or insert
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()