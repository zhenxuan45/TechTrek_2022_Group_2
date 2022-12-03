from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func



#just for user object, need to inherit UserMixin due to flask_login
#db.Model is like a general blueprint for a stored object
class User(db.Model, UserMixin):
    __tablename__ = 'User'

    userid = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True)
    password = db.Column(db.String(20))
    first_name = db.Column(db.String(255))
    last_name = db.Column(db.String(255))
    email = db.Column(db.String(255), unique=True)
    address = db.Column(db.String(255))
    OptIntoPhyStatements = db.Column(db.LargeBinary)
    
    #find all children records: find r/s with BankAccount table
    bankaccount = db.relationship('BankAccount') #mysql: referrence with cap

class BankAccount(db.Model):
    __tablename__ = 'BankAccount'

    accountid = db.Column(db.Integer, primary_key=True)
    userid = db.Column(db.Integer, db.ForeignKey('User.userid'))
    accounttype = db.Column(db.String(255))
    accountbalance = db.Column(db.Float(10,2))
    data = db.Column(db.String(10000))

    scheduledtransactions = db.relationship('ScheduledTransactions')   

class ScheduledTransactions(db.Model):
    __tablename__ = 'ScheduledTransactions'

    transactionid = db.Column(db.Integer, primary_key=True)
    accountid = db.Column(db.Integer, db.ForeignKey('BankAccount.accountid'))
    receivingaccountid = db.Column(db.Integer)
    date = db.Column(db.String(255))
    transactionamount = db.Column(db.Float(10,2))
    comment = db.Column(db.String(255))





