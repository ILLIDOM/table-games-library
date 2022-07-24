from flask_restful import Resource
from flask import request
from core.models.library_model import LibraryModel

class Library(Resource):
    def get(self, id):
        library = LibraryModel.find_by_id(id)
        if library:
            return library.json(), 200
        return {'message': 'library not found'}, 404


    def delete(self, name):
        library = LibraryModel.find_by_name(name)
        if library:
            library.delete_from_db() 
        return {'message': 'library deleted'}


class LibraryList(Resource):
    def get(self):
        return {'libraries': [library.json() for library in LibraryModel.find_all()]}


    def post(self):
        data = request.get_json()
        name = data['name']

        if LibraryModel.find_by_name(name):
            return {'message': f"Library with name {name} already exists"}, 400
        
        library = LibraryModel(name)
        try:
            library.save_to_db()
        except:
            return {'message': 'an error occured while creating the library'}, 500

        return library.json(), 201