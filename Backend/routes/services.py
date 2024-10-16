from flask import Flask
from flask import Flask, jsonify, request, abort, redirect, render_template, flash
# from flask_login import login_user, logout_user, login_required, current_user, LoginManager
from db import DB
from ..colmun.app.v1.Services.control import ServiceControl
from Backend.colmun.app.v1.core.auth import AUTH


app = Flask(__name__)#static_folder='path/to/static/folder'
app.secret_key = 'your_secret_key_here'
DB = ServiceControl()
AUTH = AUTH()


@app.route('/service', methods=['GET'], strict_slashes=False)
def get_service() -> str:
    """Return all service
    """

    return jsonify(DB.get_service()), 200


@app.route('/service', methods=['POST'], strict_slashes=False)
def create_service() ->str:
    """POST /revenue
       Return: Jsonify status 200
    """
    data = request.get_json()
    err_msg = None
    if not data:
        err_msg = 'wrong format'

    if not err_msg and data.get('name')  == "":
        err_msg = 'name is missing'
    if not err_msg and data.get('price')  == "":
        err_msg = 'price is messing'
    if not err_msg and data.get('category')  == "":
        err_msg = 'category is messing'
    if err_msg is None:
        try:
            name = data.get('name')
            price = data.get('price')
            category = data.get('category')

            service = DB.add_service(name, price, category)
            return jsonify({"message": "Service is Created"}), 200
        except Exception as e:
            err_msg = "can't create appointment: {}".format(e)
    return (f"{err_msg}")