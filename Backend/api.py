from flask import Flask
from flask import Flask, jsonify, request, abort, redirect, render_template
from flask_login import login_required
from db import DB
from auth import AUTH
from models import User, Appointment, Service, Repair, Revenue

app = Flask(__name__)
AUTH = AUTH()



@app.route('/register', methods=['POST'], strict_slashes=False)
def register_user() -> str:
    """Create new users
    """
    data = None
    error_msg = None
    try:
        data = request.form
    except Exception as e:
        data = None
    if not data:
        error_msg = 'wrong format'
    if not error_msg and data.get('email') == "":
        error_msg = 'email is missing'
    if not error_msg and data.get('password') == "":
        error_msg = 'password is messing'
    if not error_msg and data.get('role') == "":
        error_msg = 'role is missing'
    if error_msg is None:
        try:
            email = data.get('email')
            password = data.get('password')
            name = data.get('firstname')
            role = data.get('role')
            user = AUTH.register_user(email, password, name, role)
            
            if user:
                if user.role == 'mechanic':
                    redirect_url = '/mechanic.html'
                
                if user.role == 'costumer':
                    render_url = '/costumer.html'

            response = jsonify({"email": email,
                                "message": "Registered",
                                "render_url": render_url})
            return response
        except Exception:
            error_msg = "User already exist"
            response = jsonify ({'error_msg': error_msg})
    return response, 400

@app.route('/appointments', methods=['POST'], strict_slashes = False)
@login_required
def Create_appointment() -> str:
    """POST /appoitments
       Return:
       json obj with status 201
    """
    data = None
    error_msg = None
    try:
        data = request.form.get
    except Exception as e:
        data = None
    if not data:
        error_msg = 'wrong format'
    if not error_msg and data.get('date_time') == "":
        error_msg = 'date is missing'
    if not error_msg and data.get('email') == "":
        error_msg = 'customer_email is messing'
    if not error_msg and data.get('service_name') == "":
        error_msg = 'service_name is messing'
    if error_msg is None:
        try:
            date_time = data.get('date_time')
            email = data.get('email')
            customer_id = DB.get_user_id(email=email)
            name = data.get('service_name')
            service_id = DB.get_service_id(name=name)
            DB.add_appiontment(date_time, 
                                customer_id,
                                service_id)
            return jsonify({"message": "sucessfully created"}), 201
        except Exception as e:
            error_msg = "can't create appointment: {}".format(e)
    return jsonify({'error_msg': error_msg}), 400

@app.route('/appointments/history', methods=['GET'], strict_slashes=False)
def appointment_history() -> str:
    """Render the appointment history page"""
    appointments = DB.get_all_appointment()
    return render_template('appointments.html', appointments=appointments)