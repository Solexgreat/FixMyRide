from functools import wraps
from flask import request, jsonify
from ..users.control import UserControl

def authenticate(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        session_id = request.cookies.get("session_id")
        if session_id:
            user = UserControl.find_user_by_session_id(session_id)  # Check if session_id exists in the database

            if user:
                # Optionally, check if the session is expired
                request.user = user  # Add the user to the request context
                return f(*args, **kwargs)
            else:
                return jsonify({"message": "Invalid session"}), 403
        else:
            return jsonify({"message": "Token required"}), 403

    return decorated_function