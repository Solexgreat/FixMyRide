from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_security import Security, SQLAlchemyUserDatastore
from Backend.db import DB
from Backend.models import User, Appointment, Service, Repair, Revenue, Role

app = Flask(__name__)
app.config['SECRET_KEY'] = 'veryverysecret'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///FMR.db'

db = SQLAlchemy(app)

role_users = db.Table('role_users',
                    db.Column('user.id', db.Integer,db.ForeignKey('User.user_id')),
                    db.Column('role_id', db.Integer, db.ForeignKey('Role.role_id')))

user_datastore = SQLAlchemyUserDatastore(db, User, Role)

security = Security(app, db.user_datastore)

@app.route('/home')
def regsiter():
    """render index template
    """
    return render_template('index.html')

@app.route('/signup')
def regsiter():
    """render signup template
    """
    return render_template('customer-sign-up.html')