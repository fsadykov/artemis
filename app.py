from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from flask import Flask, render_template, redirect, url_for, request, jsonify
from flask_admin.contrib.sqla import ModelView
from flask_sqlalchemy  import SQLAlchemy
from flask_admin import Admin, AdminIndexView
import subprocess
import smtplib
app = Flask(__name__)

# Set up Main config
app.config['SECRET_KEY'] = 'Thisissupposedtobesecret!'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://flaskuser:flask**@104.248.212.229/fscoding'
app.config['RECAPTCHA_PUBLIC_KEY'] = '6LcpbWAUAAAAAAHfKwXV_vDW3f5gP1ET0PHsvEOp'
app.config['RECAPTCHA_PRIVATE_KEY'] = '6LcpbWAUAAAAABQidUSjPpv2K1AevKrTfSB9CYiN'
app.config['TESTING'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))



class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(15))
    lastname = db.Column(db.String(15))
    username = db.Column(db.String(15), unique=True)
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(80))
    status = db.Column(db.String(5))
    role = db.Column(db.String(5))



@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')
