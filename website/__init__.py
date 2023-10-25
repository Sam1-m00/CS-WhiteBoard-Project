from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager
db = SQLAlchemy()
DB_NAME = "database.db"

def create_app():
    app = Flask(__name__)
    app.secret_key = "this is random test secretHello"
    
    #data base location
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    
    db.init_app(app)

    from .views import views
    from .auth import auth
    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/")
    
    #create database & check if database already created
    from .models import User
    with app.app_context():
        db.create_all()

    Login_mainger = LoginManager()
    Login_mainger.login_view = 'auth.login'
    Login_mainger.init_app(app)

    @Login_mainger.user_loader
    def load_user(id):
        return User.query.get(int(id))
    
    return app