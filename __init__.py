from flask import Flask
from flask_login import current_user, login_user, logout_user
from models import User
from config import Config
from configparser import ConfigParser
# from sqlalch import db, migrate, login
from alchemy import db, migrate, login
# from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate
# from flask_login import LoginManager

# db = SQLAlchemy()
# migrate = Migrate()
# login = LoginManager()

def load_user(user_id):
    return User.query.get(int(user_id))

login.user_loader(load_user)

def create_app(config_class=Config):
    app = Flask(__name__, static_folder='static', template_folder='templates')
    from views import main
    app.register_blueprint(main)
    app.config.from_object(config_class)
    db.init_app(app)
    migrate.init_app(app, db)
    login.init_app(app)  
    
    return app
