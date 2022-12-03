from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class ScheduledTransactions(db.Model):
    transactionid = db.Column(db.Integer, primary_key=True)
    accountid = db.Column(db.Integer, db.ForeignKey('bankaccount.accountid'))
    receivingaccountid = db.Column(db.Integer)
    date = db.Column(db.String(255))
    transactionamount = db.Column(db.Decimal(10,2))
    comment = db.Column(db.String(255))

class BankAccount(db.Model):
    accountid = db.Column(db.Integer, primary_key=True)
    userid = db.Column(db.Integer, db.ForeignKey('user.userid'))
    accounttype = db.Column(db.String(255))
    accountbalance = db.Column(db.Decimal(10,2))
    data = db.Column(db.String(10000))

    scheduledtransactions = db.relationship('ScheduledTransactions')   


#just for user object, need to inherit UserMixin due to flask_login
#db.Model is like a general blueprint for a stored object
class User(db.Model, UserMixin):
    userid = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.string(20), unique=True)
    password = db.Column(db.String(20))
    first_name = db.Column(db.String(255))
    last_name = db.Column(db.String(255))
    email = db.Column(db.String(255), unique=True)
    address = db.Column(db.String(255))
    OptIntoPhyStatements = db.Column(db.LargeBinary)
    
    #find all children records: find r/s with BankAccount table
    bankaccount = db.relationship('BankAccount') #mysql: referrence with cap

