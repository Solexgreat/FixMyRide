




@app.route('/appointments', methods=['POST'], strict_slashes = False)
def Create_appointment() -> str:
    """POST /appoitments
       Return:
       json obj with status 201
    """
    data = request.form
    error_msg = None

    login_status = check_login_status()
    if login_status is False:
        return render_template('sign-in.html')
   
    if not data:
        error_msg = 'wrong format'
    if not error_msg and data.get('date_time') == "":
        error_msg = 'date is missing'
    if not error_msg and data.get('email') == "":
        error_msg = 'customer_email is missing'
    if not error_msg and data.get('name') == "":
        error_msg = 'service_name is missing'
    if not error_msg and data.get('model') == "":
        error_msg = 'enter model'
    
    if error_msg is None:
        try:
            date_time = data.get('date_time')
            email = data.get('email')
            model = data.get('model')
            customer_id = DB.get_user_id(email=email)
            name = data.get('name')
            service_id = DB.get_service_id(name=name)
            DB.add_appiontment(date_time, 
                                customer_id,
                                service_id, model)
            #return jsonify({"message": "sucessfully created"}), 201
            flash(f'sucessfully created', category='success')
            return render_template('index.html')
        except Exception as e:
            error_msg = "can't create appointment: {}".format(e)
            flash(f'{error_msg}', category='danger')

@app.route('/appointments/history', methods=['GET'], strict_slashes=False)
def appointment_history() -> str:
    """Render the appointment history page"""
    appointments = DB.get_all_appointment()
    return render_template('appointments.html', appointments=appointments)

@app.route('/appointments', methods=['GET'], strict_slashes=False)
def get_appointment() -> str:
    """Return json of all appointments
    """
    return jsonify(DB.get_all_appointment())