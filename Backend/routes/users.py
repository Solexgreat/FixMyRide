from flask import Flask, jsonify, request, abort, redirect, render_template, flash
from werkzeug.exceptions import BadRequest
# from flask_login import login_user, logout_user, login_required, current_user, LoginManager
from ..column.app.v1.users.control import UserControl
from Backend.column.app.v1.core.auth import AUTH
from . import user_bp
from ..column.app.v1.core.middleware import authenticate


DB = UserControl()


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
    data = request.get_json()
    try:
        user = AUTH.register_user(**data)
        return jsonify({'msg': f'{user.user_name} created successfully', 'token': f'{user.session_id}'}), 201
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@user_bp.route('/user', methods=['GET'], strict_slashes = False)
@authenticate
def get_users() -> str:
    """Return all users
    """
    user = request.user
    if user.role != 'admin':
        return jsonify({'msg': "Not authorized"}), 403
    return jsonify(DB.get_users()), 200

@user_bp.route('/profile', methods=['GET'], strict_slashes=False)
@authenticate
def profile() -> str:
    """GET / profile
       :Retrun
       -    use sesion_id to find user
        - 403 if session_id or user is not found
    """
    user = request.user
    if user:
        return jsonify({user}), 200
    abort(403)