from flask import Flask, jsonify, request
from models import User, Service, Appointment, Repair, Revenue
from db import DB


app = Flask(__name__)

@app.route('/user', methods=['GET'], strict_slashes = False)
def get_users() -> str:
    """Return all users
    """

    return jsonify(DB.get_users()), 200

@app.route('/service', methods=['GET'], strict_slashes=False)
def get_service() -> str:
    """Return all service
    """
    
    return jsonify(DB.get_service()), 200

@app.route('/appointments', methods=['GET'], strict_slashes=False)
def get_appointment() -> str:
    """Return json of all appointments
    """
    return jsonify(DB.get_all_appointment())

@app.route('/repairs', methods=['GET'], strict_slashes=False)
def get_repairs() -> str:
    """Return json of all repairs
    """
    return jsonify(DB.get_all_repairs())

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
            repair = DB.add_repair(date_time=date_time,
                            customer_id=customer_id, 
                            service_id=service_id, 
                            mechanic_id=mechanic_id)
            return jsonify({"message": "Repair Created"}), 200
        except Exception as e:
            err_msg = "can't create appointment: {}".format(e)

@app.route('/renvenue', methods=['GET'], strict_slashes=False)
def get_revenue() -> str:
    """Return all the Revenue property
    """
    return jsonify(DB.get_all_revenue())

@app.route('/revenue', methods=['POST'], strict_slashes=False)
def create_revenue() ->str:
    """POST /revenue
       Return: Jsonify status 200
    """
    data = request.get_json()
    err_msg = None
    if not data:
        err_msg = 'wrong format'

    if not err_msg and data.get('date_time')  == "":
        err_msg = 'date is missing'
    if not err_msg and data.get('total_appointment')  == "":
        err_msg = 'total_appointment is messing'
    if not err_msg and data.get('total_repairs')  == "":
        err_msg = 'total_repairs is messing'
    if not err_msg and data.get('total_revenue')  == "":
        err_msg = 'total_revenue is messing'
    if err_msg is None:
        try:
            date_time = data.get('date_time')
            total_appointment = data.get('total_appointment')
            total_repairs = data.get('total_repairs')
            total_revenue = data.get('total_revenue')
            revenue = DB.add_revenue(date_time=date_time,
                            total_appointment=total_appointment, 
                            total_repairs=total_repairs, 
                            total_revenue=total_revenue)
            return jsonify({"message": "Revenure Created"}), 200
        except Exception as e:
            err_msg = "can't create appointment: {}".format(e)

