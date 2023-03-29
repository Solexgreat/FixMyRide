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
    return jsonify({u.__dict__ for u in services})

@app.route('/Appointment', methods=['POST'], strict_slashes = False)
def get_appointment() -> str:
    """
    """
    data = request.get_json()
    appointment = Appointment(appointment_id=data['appointment_id'],
                               date_time=data['date_time'],
                                 customer_id=['customer_id'],
                                   service_id=['service_id'],)