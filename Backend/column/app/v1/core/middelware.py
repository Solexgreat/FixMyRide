from functools import wraps
from flask import request, jsonify

def authenticate(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        auth_header = request.headers.get('Authorization')
        if auth_header and auth_header.startswith("Bearer "):
            session_id = auth_header.split(" ")[1]
            user = db.find_user_by_session_id(session_id)  # Check if session_id exists in the database
            
            if user:
                # Optionally, check if the session is expired
                request.user = user  # Add the user to the request context
                return f(*args, **kwargs)
            else:
                return jsonify({"message": "Invalid session"}), 403
        else:
            return jsonify({"message": "Token required"}), 403

    return decorated_function