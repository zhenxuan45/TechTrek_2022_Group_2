from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func
from flask import Blueprint


class User(db.model):
    id = db.Column(db.Integer(20), primary_key=True)
    username = db.Column(db.String(20))
    password = db.Column(db.String(20))
    First_Name = db.Column(db.String(255))
    Last_Name = db.Column(db.String(255))
    email = db.Column(db.String(255))
    address = db.Column(db.String(255))
    Opt_Into_Phy_Statements = db.Column(db.LargeBinary)
    Bank_Accounts = db.relationship('BankAccount')
