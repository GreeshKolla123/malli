from app.models import Cart
from app.database import db
from app.auth import get_current_user

def get_cart(user: User):
    return db.query(Cart).filter(Cart.user_id == user.id).all()

def add_to_cart(user: User, product_id: int, quantity: int):
    cart = Cart(user_id=user.id, product_id=product_id, quantity=quantity)
    db.add(cart)
    db.commit()
    db.refresh(cart)
    return cart

def remove_from_cart(user: User, product_id: int):
    cart = db.query(Cart).filter(Cart.user_id == user.id).filter(Cart.product_id == product_id).first()
    if cart:
        db.delete(cart)
        db.commit()
    return