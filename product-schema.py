
from app import ma
#product SQLALCHEMY_DATABASE_URI
class ProductSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'description', 'price', 'qty')

#init Schema
product_schema = ProductSchema()
products_schema = ProductSchema(many=True)
