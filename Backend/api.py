from flask import Flask
from flask import Flask, jsonify, request, abort, redirect, render_template, flash
from flask_login import login_user, logout_user, login_required, current_user, LoginManager
from db import DB
from Backend.colmun.app.v1.core.auth import AUTH


app = Flask(__name__)#static_folder='path/to/static/folder'
app.secret_key = 'your_secret_key_here'
DB = DB()
AUTH = AUTH()
login_manager = LoginManager(app)
login_manager.login_view = "login"













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

@app.route('/sign-up.html')
def sign_up():
    """
    """
    return render_template('sign-up.html')

@app.route('/templates/sign-in.html')
@app.route('/sign-in.html')
def sign_in():
    """
    """
    return render_template('sign-in.html')

@app.route('/admin-dashboard.html')
def admin():
    """
    """
    return render_template('admin-dashboard.html')

@app.route('/index.html')
def index():
    """
    """
    return render_template('index.html')
    
if __name__ == "__main__":
    app.run(port="5000", debug=True)