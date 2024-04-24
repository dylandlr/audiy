# OAUTH2_DOMAIN=dev-dyl.us.auth0.com
# OAUTH2_Redirect_URI=http://localhost:3000/callback
# Auth0 Configuration and Flask Configuration
# FEATURES:
# This file is used to configure the Auth0 and Flask settings for the application.
# The Auth0 configuration includes the domain and client ID for the Auth0 application, which are used to authenticate users.
# The Flask configuration includes the secret key, which is used to encrypt session data, and the redirect URI, which is used to redirect users after they log in or log out.
# The configuration settings are loaded from environment variables, which are set in the .env file in the root directory of the project.

# TEMPLATE:

from flask import Flask
from views import main
from config import Config
from configparser import ConfigParser
from flask_login import current_user, login_user, logout_user
from models import User
from audit_data import audit_features
from __init__ import create_app


app = create_app(Config)

# print(audit_features)
# app.secret_key = os.getenv('SQLALCHEMY_SECRET_KEY')

#run the sqlite database

# if not os.path.exists('audit_list.db'):
#     sqlite_db.init_db()  
    
# initialize the database with the audit features data s
# meaning it will create the audit_list.db file and the audit_list table with the audit features data
# so that you dont have to run the sqlite_db.py file separately to create the database and table




if __name__ == '__main__':
    app.run(debug=True)


    
    
