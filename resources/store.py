from flask_restful import Resource
from models.store import StoreModel

class Store(Resource):
    def get(self,name):
        store =  StoreModel.find_by_name(name)
        if store:
            return store.json()
        else:
            {"message":"Store does not exist"}
    def post(self,name):
        if StoreModel.find_by_name(name):
            return {"message":"Store {} already exists".format(name)}
        else:
            store = StoreModel(name)
            return store.save_to_db()
    def delete(self,name):
        store = StoreModel.find_by_name(name)
        if store:
            return store.delete_from_db()
        else:
            return {"message":"store does not exist"}
class StoreList(Resource):
    def fet(self):
        return {"stores": store.json() for store in StoreModel.query.all()}