from flask import Flask,request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from datetime import datetime
import os

#init app
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))

#database
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:mypassr@localhost/store_db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+ os.path.join(basedir,'store_db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#init db
db = SQLAlchemy(app)

#init ma
ma = Marshmallow(app)

#product class
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    price = db.Column(db.Float)
    qty = db.Column(db.Integer)

    def __init__(self, name, price, description, qty):
        self.name = name
        self.description = description
        self.price = price
        self.qty = qty
        
       # super().__init__()

#product SQLALCHEMY_DATABASE_URI
class ProductSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'description', 'price', 'qty')

#init Schema
product_schema = ProductSchema()
products_schema = ProductSchema(many=True)

#create a product
@app.route('/api/product/create', methods=['POST'])
def add_product():
    name = request.json['name']
    desc   = request.json['desc']
    price = request.json['price']
    qty = request.json['qty']

    new_product = Product(name, price, desc, qty)
    db.session.add(new_product)
    db.session.commit()
    return product_schema.jsonify(new_product)

#get all products
@app.route('/api/products', methods=['GET'])
def get_products():    
    all_products = Product.query.all()
    result = products_schema.dump(all_products)
    return jsonify(result)

#Get single product
@app.route('/api/product/<id>', methods=['GET'])
def get_product(id):
    product = Product.query.first()
    return product_schema.jsonify(product)

def getCurrentDate():
    now = datetime.now()
    return now.strftime("%d-%m-%Y %H:%M:%S")

#run server
if __name__ == '__main__':
    app.run(debug=True)