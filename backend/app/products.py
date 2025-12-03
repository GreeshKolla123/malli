from app.models import Product
from app.database import db

def get_products):
    return db.query(Product).all()

def get_product(id: int):
    return db.query(Product).filter(Product.id == id).first()