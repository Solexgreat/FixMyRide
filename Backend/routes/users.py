from flask import Flask
from flask import Flask, jsonify, request, abort, redirect, render_template, flash
# from flask_login import login_user, logout_user, login_required, current_user, LoginManager
from ..column.app.v1.users.control import UserControl
from Backend.column.app.v1.core.auth import AUTH
from . import user_bp


DB = UserControl()
AUTH = AUTH()


# @login_manager.user_loader
def load_user(user_id):
    """
    """
    user = DB.find_user(user_id=user_id)
    if user is None:
        return None

@user_bp.route('/register', methods=['POST'], strict_slashes=False)
def register_user() -> str:
    """Creat new user
    """

    name = request.form['first name']
    email = request.form['email']
    password = request.form['password']
    role = request.form['role']
    try:
        user = AUTH.register_user(email, password, name, role)
    except Exception as e:
        return flash(f'user already exist', category='danger')
    # login_user(user)
    if user:
        if user.role == 'Admin':
            return render_template('admin-dashboard.html')

        if user.role == 'Costumer':
            return render_template('index.html')
    else:
        flash(f'user already exist', category='danger')


@user_bp.route('/user', methods=['GET'], strict_slashes = False)
def get_users() -> str:
    """Return all users
    """

    return jsonify(DB.get_users()), 200

@user_bp.route('/profile', methods=['GET'], strict_slashes=False)
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