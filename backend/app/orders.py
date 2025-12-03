from app.models import Order, OrderItem
from app.database import db
from app.auth import get_current_user

def place_order(user: User, payment_method: str):
    order = Order(user_id=user.id, total=0, status="pending")
    db.add(order)
    db.commit()
    db.refresh(order)
    return order

def get_orders(user: User):
    return db.query(Order).filter(Order.user_id == user.id).all()