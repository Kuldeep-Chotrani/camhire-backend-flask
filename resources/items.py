import sqlite3

from flask_restful import Resource, reqparse
from flask_jwt import  jwt_required
from models.item import ItemModel


class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price',
                        type=float,
                        required=True,
                        help="this is required field")
    parser.add_argument('store_id',
                        type=int,
                        required=True,
                        help="Every item needs a store")
    def get(self,name):
        item = ItemModel.find_by_name(name)
        if item:
            return item.json()
        return {"ITEM": "Does not exists"}, 404

    def post(self,name):
        item = ItemModel.find_by_name(name)
        if item:
            return {name: "Already exist"}
        else:
            data = Item.parser.parse_args()
            item = ItemModel(name,**data)
            try:
                item.save_to_db()
            except():
                return {"message":"error occured in database"}, 500
            return item.json(), 201
    @jwt_required()
    def delete(self,name):
        item = ItemModel.find_by_name(name)
        if item:
            item.delete_from_db()
        return {'message':"Item Deleted"}
    def put(self,name):
        item = ItemModel.find_by_name(name)
        data = Item.parser.parse_args()
        if item:
            item = ItemModel(name,**data)
        else:
            item.price = data['price']
        item.save_to_db()
        return item.json()
class ItemList(Resource):
    def get(self):
        return {'item':[item.json() for item in ItemModel .query.all()]}
    #list(map(lambda x:x.json,ItemModel.query.all())