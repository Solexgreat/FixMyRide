from flask import Flask
from flask import Flask, jsonify, request, abort, redirect, render_template, flash
from flask_login import login_user, logout_user, login_required, current_user, LoginManager
from db import DB
from Backend.colmun.app.v1.core.auth import AUTH


app = Flask(__name__)#static_folder='path/to/static/folder'
app.secret_key = 'your_secret_key_here'
DB = DB()
AUTH = AUTH()
login_manager = LoginManager(app)
login_manager.login_view = "login"



if __name__ == "__main__":
    app.run(port="5000", debug=True)