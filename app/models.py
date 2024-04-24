# models.py
# here we define the User model, which represents the users of the application.
# The User model includes fields for the user's username, email, and password, as well as methods for password hashing and checking.
# The User model also includes a method to check if the user is an authenticated user.
#
from werkzeug.security import generate_password_hash, check_password_hash
from alchemy import db
from flask_login import UserMixin

def generate_password_hash(password):
    return generate_password_hash(password)

def check_password_hash(password, hash):
    return check_password_hash(password, hash)

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(password, self.password_hash)

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.id)