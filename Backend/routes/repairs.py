from flask import Flask
from flask import Flask, jsonify, request, abort, redirect, render_template, flash
# from flask_login import login_user, logout_user, login_required, current_user, LoginManager
from db import DB
from ..colmun.app.v1.Repairs.control import RepairControl
from Backend.colmun.app.v1.core.auth import AUTH


app = Flask(__name__)#static_folder='path/to/static/folder'
app.secret_key = 'your_secret_key_here'
DB = RepairControl()
AUTH = AUTH()



@app.route('/repairs', methods=['GET'], strict_slashes=False)
def get_repairs() -> str:
    """Return json of all repairs
    """
    return jsonify(DB.get_all_repairs())

@app.route('/repairs', methods=['POST'], strict_slashes = False)
def create_repairs() -> str:
    """POST /repairs
       Return: Jsonify(message) status 200
    """
    data = request.get_json()
    err_msg = None
    if not data:
        err_msg = 'wrong format'

    if not err_msg and data.get('date_time')  == "":
        err_msg = 'date is missing'
    if not err_msg and data.get('customer_id')  == "":
        err_msg = 'customer_id is messing'
    if not err_msg and data.get('service_id')  == "":
        err_msg = 'service_id is messing'
    if err_msg is None:
        try:
            date_time = data.get('date_time')
            customer_id = data.get('customer_id')
            service_id = data.get('service_id')
            mechanic_id = data.get('mechanic_id')
            repair = DB.add_repair(date_time,
                            customer_id, 
                            service_id, 
                            mechanic_id)
            return jsonify({"message": "Repair Created"}), 200
        except Exception as e:
            err_msg = "can't create appointment: {}".format(e)
    return (f"{err_msg}")