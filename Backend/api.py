from flask import Flask
from flask import Flask, jsonify, request, abort, redirect
from db import DB
from auth import AUTH
from models import User, Appointment, Service, Repair, Revenue

app = Flask(__name__)
AUTH = AUTH()

@app.route('/register', methods=['POST'], strict_slashes=False)
def register_user() -> str:
    """
    """
    data = None
    error_msg = None
    try:
        data = request.get_json()
    except Exception as e:
        data = None
    if not data:
        error_msg = 'wrong format'
    if not error_msg and data.get('email') == "":
        error_msg = 'email is missing'
    if not error_msg and data.get('password') == "":
        error_msg = 'password is messing'
    if error_msg is None:
        try:
            email = data['email']
            password = data['password']
            user = AUTH.register_user(email, password)
            return jsonify({"message": "appointment suseccfully create"}), 201
        except Exception:
            error_msg = "User already exist"
    return (f"{error_msg}"), 400

@app.route('/appointments', methods=['POST'], strict_slashes = False)
def Create_appointment() -> str:
    """POST /appoitments
       Return:
       json obj with status 201
    """
    data = None
    error_msg = None
    try:
        data = request.get_json()
    except Exception as e:
        data = None
    if not data:
        error_msg = 'wrong format'
    if not error_msg and data.get('date_time') == "":
        error_msg = 'date is missing'
    if not error_msg and data.get('customer_id') == "":
        error_msg = 'customer_id is messing'
    if not error_msg and data.get('service_id') == "":
        error_msg = 'service_id is messing'
    if error_msg is None:
        try:
            date_time = data['date_time']
            customer_id = data['customer_id']
            service_id = data['service_id']
            DB.add_appiontment(date_time=date_time, 
                                customer_id=customer_id,
                                service_id=service_id)
            return jsonify({"message": "appointment suseccfully create"}), 201
        except Exception as e:
            error_msg = "can't create appointment: {}".format(e)
    return (f"{error_msg}") 400