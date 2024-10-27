from flask import Flask
from flask import Flask, jsonify, request, abort, redirect, render_template, flash
# from flask_login import login_user, logout_user, login_required, current_user, LoginManager
from ..column.app.v1.Appointments.control import AppointmentControl
from Backend.column.app.v1.core.auth import AUTH
from . import appointment_bp
from ..db import DB
from ..column.app.v1.core.middleware import authenticate


db_instance = DB()
db = AppointmentControl()
auth = AUTH()


@appointment_bp.route('/appointments', methods=['POST'], strict_slashes = False)
@authenticate
def Create_appointment() -> str:
    """POST /appoitments
       Return:
       json obj with status 201
    """
    data = request.get_json()
    error_msg = None
    user_id = request.user.user_id

    # login_status = check_login_status()
    # if login_status is False:
    #     return render_template('sign-in.html')

    if not data:
        error_msg = 'wrong format'
    if not error_msg and data.get('service_id') == "":
        error_msg = 'service_id is missing'
    if not error_msg and data.get('model') == "":
        error_msg = 'enter car model'

    if error_msg is None:
        try:
            date_time = None
            model = data.get('model')
            customer_id = user_id
            service_id = data.get('service_id')
            status = data.get('status')
            appointment = db.add_appointment(date_time,
                                customer_id,
                                service_id, model, status)
            return jsonify({"message": "sucessfully created", 'appointment_id': f'{appointment.appointment_id}'}), 201
        except Exception as e:
            return jsonify({'msg': 'Internal error', 'error': str(e)}), 500

@appointment_bp.route('/appointment/history', methods=['GET'], strict_slashes=False)
@authenticate
def appointment_history() -> str:
    """Render the appointment history page"""
    try:
        user_id = request.user.user_id
        role = request.user.role

        appointments = db.get_all_appointments(user_id, role)
        return jsonify({'Appointments' : appointments}), 201
    except Exception as e:
        return jsonify({'error' : str(e)}), 500

@appointment_bp.route('/appointment/history_between', methods=['GET'], strict_slashes=False)
@authenticate
def appointment_history_between() -> str:
    """Render the appointment history page"""
    try:
        data = request.get_json()
        initial_date = data.get('initial_date')
        current_date = data.get('current_date')
        role = request.user.role

        #Check if user is an admin
        if role != 'admin':
            return jsonify({'msg': 'unauthorised user'}), 403

        appointments = db.get_appointment_between_dates(initial_date, current_date)
        return jsonify({'Appointments' : appointments}), 201
    except Exception as e:
        return jsonify({'error' : str(e)}), 500

@appointment_bp.route('/appointment/completed_between', methods=['GET'], strict_slashes=False)
@authenticate
def appointment_history_between() -> str:
    """Render the appointment history page"""
    try:
        data = request.get_json()
        initial_date = data.get('initial_date')
        current_date = data.get('current_date')
        role = request.user.role

        #Check if user is an admin
        if role != 'admin':
            return jsonify({'msg': 'unauthorised user'}), 403

        appointments = db.get_completed_appointment_between_dates(initial_date, current_date)
        return jsonify({'Appointments' : appointments}), 201
    except Exception as e:
        return jsonify({'error' : str(e)}), 500

@appointment_bp.route('/appointment/<int:appointment_id>', methods=['GET'], strict_slashes=False)
@authenticate
def get_appointment(appointment_id) -> str:
    """Return json of all appointments
    """
    user = request.user
    role = user.role
    user_id = user.user_id
    try:
        appointment = db.get_appointments(appointment_id, user_id, role)
        return jsonify(appointment)
    except Exception as e:
        return jsonify({'error': f'{e}'}), 500

@appointment_bp.route('/update_appointment/<int:appointment_id>', methods=['PUT'], strict_slashes=False)
@authenticate
def update_appointment(appointment_id) -> str:
    """Return json of all appointments
    """

    data = request.get_json()
    try:
        # db_instance.add_column('appointment', 'mechanic_id', 'INETGER')
        if not data:
            return jsonify({'msg': 'request is empty'}), 400
        appointment = db.update_appointment(appointment_id, **data)
        return jsonify({'msg': 'Appointment updated successfuly', 'appointment_id': f'{appointment.appointment_id}'})
    except Exception as e:
        return jsonify({'msg': 'Internal error', 'error': str(e)}), 500