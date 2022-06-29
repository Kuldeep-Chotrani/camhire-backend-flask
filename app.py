import os

from flask import Flask, send_from_directory, abort
from flask_restful import Api
from flask_jwt import JWT
from resources.items import Item, ItemList
from resources.photographers import Photographers, PhotographerList
from resources.user import UserRegister
from security import authenticate,identity
from resources.store import Store,StoreList
from db import db
app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQlALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['data_of_photographers'] = "/home/kuldeepchotrani/Desktop/git_project/sample-app/updated/pdf"
app.secret_key = "kuldeep"
jwt = JWT(app,authenticate,identity)
items = []
@app.before_first_request
def create_table():
    db.create_all()

db.init_app(app)
api.add_resource(Item,'/item/<string:name>')
api.add_resource(ItemList,'/items')
api.add_resource(StoreList,'/stores')
api.add_resource(Store,'/store/<string:name>')
api.add_resource(Photographers,'/photographer/<string:name>')
api.add_resource(PhotographerList,'/photographers')
@app.route("/get-pdf/<pdf_name>")
def get_pdf(pdf_name):
    try:
        return send_from_directory(app.config['data_of_photographers'], path=pdf_name, as_attachment=True)
    except:
        abort(404)

api.add_resource(UserRegister,'/register')
app.run()