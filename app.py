from flask import Flask,request, jsonify
import flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from datetime import date,datetime
from flask_pymongo import PyMongo
from pymongo.errors import BulkWriteError

import os

#init app
app = Flask(__name__)
#basedir = os.path.abspath(os.path.dirname(__file__))

#database
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:123-Aquifer@localhost/ikenna_db'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+ os.path.join(basedir,'ikenna_db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
mongodb_client = PyMongo(app, uri="mongodb://localhost:27017/flask_db")
db = mongodb_client.db

#init db
#db = SQLAlchemy(app)

#init ma
#ma = Marshmallow(app)

#product class
# class Product(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(100), unique=True)
#     price = db.Column(db.Float)
#     qty = db.Column(db.Integer)

#     def __init__(self, name, price, description, qty):
#         self.name = name
#         self.description = description
#         self.price = price
#         self.qty = qty
        
       # super().__init__()

#product SQLALCHEMY_DATABASE_URI
# class ProductSchema(ma.Schema):
#     class Meta:
#         fields = ('id', 'name', 'description', 'price', 'qty')

#init Schema
# product_schema = ProductSchema()
# products_schema = ProductSchema(many=True)

#create a product
@app.route('/api/product/create', methods=['POST'])
def add_product():
    try:    
        db.flask_db.insert_many([
            {'title': "title one ", 'body': "todo body one "},
            {'title': "title two", 'body2': "todo body two"},
            {'title': "title three", 'body3': "todo body three"},
            {'title': "title four", 'body4': "todo body four"},
            {'title': "title five", 'body5': "todo body five"},
            {'title': "title six", 'body6': "todo body six"},
            ])
        return flask.jsonify(message="success")
    except BulkWriteError as bwe:
        print(bwe.details)
        #you can also take this component and do more analysis
        #werrors = bwe.details['writeErrors']
        raise

def getCurrentDate():
    now = datetime.now()
    return now.strftime("%d-%m-%Y %H:%M:%S")

#run server
if __name__ == '__main__':
    app.run(debug=True)