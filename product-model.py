from app import db

#product class
class Product(db.Model):
    id = db.Column(db.Interger, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    price = db.Column(db.float)
    qty = db.Column(db.Interger)

    def __init__(self, name, price, description, qty) -> None:
        self.name = name
        self.description = description
        self.price = price
        self.qty = qty
        
        super().__init__()