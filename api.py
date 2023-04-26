from flask import Flask
from flask import Flask, jsonify, request, abort, redirect, render_template, flash
from flask_login import login_user, logout_user, login_required, current_user, LoginManager
from db import DB
from auth import AUTH


app = Flask(__name__)
app.secret_key = 'your_secret_key_here'
DB = DB()
AUTH = AUTH()
login_manager = LoginManager(app)
login_manager.login_view = "login"


@login_manager.user_loader
def load_user(user_id):
    """
    """
    user = DB.find_user(user_id=user_id)
    if user is None:
        return None

@app.route('/register', methods=['POST'], strict_slashes=False)
def register_user() -> str:
    """Creat new user
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
            login_user(user)
            
            if user:
                if user.role == 'mechanic':
                    return render_template('mechanic.html')
                
                if user.role == 'costumer':
                    return render_template('costumer.html')
        except Exception:
            error_msg = "User already exist"
    return jsonify ({'error_msg': error_msg}), 400

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

    if not err_msg and data.get('date_time') == "":
        err_msg = 'date is missing'
    if not err_msg and data.get('total_appointment') == "":
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
            revenue = DB.add_revenue(date_time,
                            total_appointment, 
                            total_repairs, 
                            total_revenue)
            return jsonify({"message": "Revenure Created"}), 200
        except Exception as e:
            err_msg = "can't create appointment: {}".format(e)
    return jsonify({'err_msg': err_msg})

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

@app.route('/sessions', methods=['POST'], strict_slashes=False)
def login() -> str:
    """Validate the Login info
       and create a login session
    """
    email = request.form.get('email')
    password = request.form.get('password')

    user = AUTH.valid_loggin(email, password)
    if user:
        session_id = AUTH.create_session(email)
        response = jsonify({"email": email,
                            "message": "logged in"})
        response.set_cookie("session_id", session_id)
        if user:
            if user.role == 'admin':
                return render_template('admin-dashboard.html')
            
            if user.role == 'costumer':
               return render_template('index.html')
        return response
    else:
        abort(401)

@app.route('/logout', methods=['DELETE'], strict_slashes=False)
def logout():
    """Logout and destroy session
    """
    session_id = request.cookies.get('session_id')
    user = AUTH.get_user_from_session_id(session_id)
    if not user:
        return None
    
    AUTH.destroy_session(user.user_id)
    return redirect('/')

@app.route('/profile', methods=['GET'], strict_slashes=False)
def profile() -> str:
    """GET / profile
       :Retrun
       -    use sesion_id to find user
        - 403 if session_id or user is not found
    """
    session_id = request.cookies.get("session_id")
    if session_id is None:
        abort(403)
    user = AUTH.get_user_from_session_id(session_id)
    if user:
        return jsonify({"email": user.email}), 200
    abort(403)

@app.route('/reset_password', methods=['POST'], strict_slashes=False)
def get_reset_password_token() -> str:
    """POST /reset_password
        :Return
        -status 403 if email is invalid
    """
    email = request.form.get('email') 
    reset_token = AUTH.get_reset_password_token(email)
    if reset_token:
        return jsonify({"email": email, "reset_token": reset_token}), 200
    else:
        abort(403)

@app.route('/reset_password', methods=['PUT'], strict_slashes=False)
def update_password() -> str:
    """PUT /reset_password
       :Return
       -status 403 if token is invalid
    """
    email = request.form.get(email)
    new_password = request.form.get(new_password)
    reset_token = request.form.get(reset_token)
    try:
        AUTH.update_password(reset_token, new_password)
    except Exception:
        abort(403)

    return jsonify({"email": email, "message": "Password updated"}), 200

@app.route('/api/check_login_status', methods=['GET'])
def check_login_status():
    # Check if session_id cookie is present
    session_id = request.cookies.get('session_id')
    if session_id:
        # Verify session_id with AUTH class
        if AUTH.get_user_from_session_id(session_id):
            return True
        else:
            return False
    else:
        return False
    
if __name__ == "__main__":
    app.run(port="5000", debug=True)