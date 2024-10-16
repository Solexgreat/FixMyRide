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