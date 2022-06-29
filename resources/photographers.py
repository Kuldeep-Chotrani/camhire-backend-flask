import sqlite3

from flask_restful import Resource, reqparse
from flask_jwt import  jwt_required
from flask import send_from_directory,abort
from models.photographer import PhotographerModel


class Photographers(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('speciality',
                        type=str,
                        required=True,
                        help="this is required field")

    parser.add_argument('description',
                        type=str,
                        required=True,
                        help="this is required field")
    def get(self,name):
        photographer = PhotographerModel.find_by_name(name)
        if photographer:
            return photographer.json()
        return {"ITEM": "Does not exists"}, 404

    def post(self,name):
        photographer = PhotographerModel.find_by_name(name)
        if photographer:
            return {name: "Already exist"}
        else:
            data = Photographers.parser.parse_args()
            photographer = PhotographerModel(name,**data)
            try:
                photographer.save_to_db()
            except():
                return {"message":"error occured in database"}, 500
            return photographer.json(), 201
    @jwt_required()
    def delete(self,name):
        photographer = PhotographerModel.find_by_name(name)
        if photographer:
            photographer.delete_from_db()
        return {'message':"Item Deleted"}
    def put(self,name):
        photographer = PhotographerModel.find_by_name(name)
        data = Photographers.parser.parse_args()
        if photographer:
            photographer = PhotographerModel(name,**data)
        else:
            photographer.speciality = data['speciality']
        photographer.save_to_db()
        return photographer.json()
class PhotographerList(Resource):
    def get(self):
        return {'photographer':[photographer.json() for photographer in PhotographerModel.query.all()]}
    #list(map(lambda x:x.json,ItemModel.query.all())