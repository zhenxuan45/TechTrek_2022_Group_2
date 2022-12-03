from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func
from flask import Blueprint

# models=Blueprint("models",__name__)

class User(db.Model, UserMixin): 
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(10), unique=True)
    password = db.Column(db.String(150)) 
    first_name = db.Column(db.String(150))
    last_name = db.Column(db.String(150))
    email = db.Column(db.String(150), unique=True)
    address = db.Column(db.String(200))
    optphy = db.Column(db.Boolean())
    transactions = db.relationship('Transaction')


class Transaction(db.Model): 
    id = db.Column(db.Integer, primary_key=True) 
    data = db.Column(db.String(15000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    