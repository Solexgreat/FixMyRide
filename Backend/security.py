
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_security import Security, SQLAlchemyUserDatastore
from db import DB

user_datastore = SQLAlchemyUserDatastore()