# views.py

from flask import Flask, Blueprint, render_template, request, redirect, url_for, flash
# from app import auth
from audit_data import audit_features
from flask_login import current_user, login_user, logout_user
from models import User
from config import Config
from configparser import ConfigParser
from sqlalch import db, migrate, login

# Define the main Blueprint for the application
# Blueprint is a way to organize a group of related views and other code and is separate from the main application instance.
# This allows for better organization and separation of concerns in the application.
# we call the Blueprint constructor and pass in the name to specify the Blueprint and the module or package where the Blueprint is defined.
# __name__ is a special Python variable that is set to the name of the current module. 
# we can change the name of the Blueprint to something else if we want to. by default, the name of the Blueprint is used as the prefix for the routes defined in the Blueprint.
# For example, if the name of the Blueprint is 'main', then the route /index in the Blueprint will be /main/index.
main = Blueprint('main', __name__)

# Define the index route, which renders the index.html from /templates
# i.e the homepage, or landing page of the web application

@main.route('/')
def index():
    return render_template('index.html')


# Define the audit route, which renders the audit.html from /templates
# i.e the page that displays the audit features and their compliance status
# they can be checked off as compliant or not compliant and list
# the importance of the feature, and a description of the feature's requirements
@main.route('/audit')
def show_audit():
    return render_template('audit.html', audit_features=audit_features)

@main.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    if request.method == 'POST':
        user = User.query.filter_by(username=request.form['username']).first()
        if user is not None and user.check_password(request.form['password']):
            login_user(user, remember=request.form.get('remember_me', False))
            return redirect(url_for('main.index'))
    return render_template('login.html')

@main.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main.index'))

@main.route('/signup', methods=['GET', 'POST'])
def signup():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    if request.method == 'POST':
        user = User(username=request.form['username'], email=request.form['email'])
        user.set_password(request.form['password'])
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('main.login'))
    return render_template('signup.html')

@main.route('/profile')
def profile():
    return render_template('profile.html')

@main.route('/about')
def about():
    return render_template('about.html')

@main.route('/contact')
def contact():
    return render_template('contact.html')

@main.route('/audit-report')
def audit_report():
    compliant_count = sum(1 for f in audit_features if f['compliance'])
    total_features = len(audit_features)
    return render_template('report.html', compliant_count=compliant_count, total_features=total_features)

@main.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

if __name__ == '__main__':
    main.run(debug=True)