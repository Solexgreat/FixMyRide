from flask import Flask, jsonify, request, abort, redirect, render_template, flash
from werkzeug.exceptions import BadRequest
# from flask_login import login_user, logout_user, login_required, current_user, LoginManager
from ..column.app.v1.users.control import UserControl
from Backend.column.app.v1.core.auth import AUTH
from . import user_bp


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
    except BadRequest as e:
		return jsonify({"error": str(e)}), 400
    except Exception as e:
        return jsonify({'msg': ""})


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
    user = AUTH.get_current_user(session_id)
    if user:
        return jsonify({"email": user.email}), 200
    abort(403)