from flask_restful import Resource
from core.models.library_model import LibraryModel

class Library(Resource):
    def get(self, name):
        library = LibraryModel.find_by_name(name)
        if library:
            return library.json(), 200
        return {'message': 'store not found'}, 404


    def post(self, name):
        if LibraryModel.find_by_name(name):
            return {'message': f"Store with name {name} already exists"}, 400
        
        library = LibraryModel(name)
        try:
            library.save_to_db()
        except:
            return {'message': 'an error occured while creating the library'}, 500

        return library.json(), 201


    def delete(self, name):
        library = LibraryModel.find_by_name(name)
        if library:
            library.delete_from_db() 
        return {'message': 'library deleted'}


class LibraryList(Resource):
    def get(self):
        return {'libraries': [library.json() for library in LibraryModel.find_all()]}