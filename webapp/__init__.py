from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
from os import path

db=SQLAlchemy()
DB_NAME = "database.db" 

def create_app(): 
   
    app=Flask(__name__)
    app.config['SECRET_KEY']='testsecretkey'
    app.config['SQLALCHEMY_DATABASE_URI']=f'sqlite:///{DB_NAME}'
    db.init_app(app)
    

    from .models import User, BankAccount

    # BankAccount, ScheduledTransactions
    
    # app.register_blueprint(models,url_prefix='/')


    # if not path.exists('instance/'+ DB_NAME): 
    with app.app_context():
        db.create_all()
        print(db)
        print('Created Database')

    return app 

