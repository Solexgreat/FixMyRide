from flask import Flask, jsonify, request
from models import User, Service, Appointment, Repair, Revenue
from db import DB


app = Flask(__name__)

@app.route('/user', methods=['GET'], strict_slashes = False)
def get_users() -> str:
    """Return all users
    """
    users = DB.all(User)

    return jsonify({u.__dict__ for u in users})

@app.route('/service', methods=['GET'], strict_slashes = False)
def get_service() -> str:
    """Return all service
    """
    services = DB.all(Service)
    return jsonify({u.__dict__ for u in services}), 200

@app.route('/appointments', methods=['POST'], strict_slashes = False)
def get_appointment() -> str:
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
            appointment = DB.add_appiontment(date_time=date_time, 
                                            customer_id=customer_id,
                                            service_id=service_id)
            return jsonify({appointment.__dict__}), 201
        except Exception as e:
            error_msg = "can't create appointment: {}".format(e)

@app.route('/repairs', methods=['GET'], strict_slashes = False)
def get_repairs() -> str:
    """
    """
    data = request.get_json()

    date_time = data.get('date_time')
    customer_id = data.get('customer_id')
    service_id = data.get('service_id')
    mechanic_id = data.get('service_id')

    repair = DB.add_repair(date_time=date_time,
                            customer_id=customer_id, 
                            service_id=service_id, 
                            mechanic_id=mechanic_id)
    return jsonify({repair.__dict__})

