from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.requests import Request
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from app.models import Base, User, Product, Cart, Order, OrderItem
from app.database import engine, SessionLocal
from app.auth import authenticate_user, get_current_user
from app.cart import get_cart, add_to_cart, remove_from_cart
from app.orders import place_order, get_orders
from app.products import get_products, get_product
from app.users import get_users, create_user, get_user

app = FastAPI()

@app.post("/api/register")
def register_user(username: str, email: str, password: str):
    return create_user(username, email, password)

@app.post("/api/login")
def login_user(username: str, password: str):
    return authenticate_user(username, password)

@app.get("/api/products")
def read_products(current_user: User = Depends(get_current_user)):
    return get_products()

@app.get("/api/products/{id}")
def read_product(id: int, current_user: User = Depends(get_current_user)):
    return get_product(id)

@app.post("/api/cart")
def add_to_cart(product_id: int, quantity: int, current_user: User = Depends(get_current_user)):
    return add_to_cart(current_user, product_id, quantity)

@app.get("/api/cart")
def read_cart(current_user: User = Depends(get_current_user)):
    return get_cart(current_user)

@app.post("/api/checkout")
def place_order(payment_method: str, current_user: User = Depends(get_current_user)):
    return place_order(current_user, payment_method)

@app.get("/api/orders")
def read_orders(current_user: User = Depends(get_current_user)):
    return get_orders(current_user)