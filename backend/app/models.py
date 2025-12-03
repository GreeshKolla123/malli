from sqlalchemy import Column, Integer, String, Float
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from pydantic import BaseModel
from typing import Optional

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True)
    email = Column(String, unique=True)
    password = Column(String)
    cart = relationship("Cart", backref="user")
    orders = relationship("Order", backref="user")

    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"

class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    price = Column(Float)
    cart = relationship("Cart", backref="product")
    orders = relationship("OrderItem", backref="product")

    def __repr__(self):
        return f"Product('{self.name}', '{self.description}', '{self.price}')"

class Cart(Base):
    __tablename__ = 'cart'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    product_id = Column(Integer, ForeignKey('products.id'))
    quantity = Column(Integer)

    def __repr__(self):
        return f"Cart('{self.user_id}', '{self.product_id}', '{self.quantity}')"

class Order(Base):
    __tablename__ = 'orders'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    total = Column(Float)
    status = Column(String)
    items = relationship("OrderItem", backref="order")

    def __repr__(self):
        return f"Order('{self.user_id}', '{self.total}', '{self.status}')"

class OrderItem(Base):
    __tablename__ = 'order_items'
    id = Column(Integer, primary_key=True)
    order_id = Column(Integer, ForeignKey('orders.id'))
    product_id = Column(Integer, ForeignKey('products.id'))
    quantity = Column(Integer)

    def __repr__(self):
        return f"OrderItem('{self.order_id}', '{self.product_id}', '{self.quantity}')"