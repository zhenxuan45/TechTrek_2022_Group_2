
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

#setting up of database
db = SQLAlchemy()
DB_NAME = "database.db"

#creating flask application
def create_app():
    app = Flask(__name__)

    #flask configuration
    #secret_key: encrypt/decrypt session cookies
    app.config['SECRET_KEY'] = 'testsecretkey'
    #location of database
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    #initialise database - app uses this database db
    db.init_app(app)
    
    #import of blueprint
    from .views import views
    from .auth import auth

    #register blueprint, url_prefix must be contained in the route
    app.register_blueprint(views, url_prefix = '/')
    # app.register_blueprint(views, url_prefix = '/auth/')
    app.register_blueprint(auth, url_prefix = '/')

    
    #this should be run first and define classes before initializing database
    from .models import User, Note
    
    create_database(app)

    login_manager = LoginManager()
    #where should flask redirect user if not logged in and log in is required
    login_manager.login_view = 'auth.login' 
    login_manager.init_app(app)

    #how we load user
    @login_manager.user_loader
    def load_user(id):
        #which user we are looking for/load 
        return User.query.get(int(id))

    return app

def create_database(app):
    if not path.exists('./' + DB_NAME):
        #creating database for app
        db.create_all(app=app)
        print('Created Database!')