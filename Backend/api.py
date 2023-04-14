from flask import Flask
from flask import Flask, jsonify, request, abort, redirect
from db import DB
from auth import AUTH
from models import User, Appointment, Service, Repair, Revenue

app = Flask(__name__)
AUTH = AUTH()


@app.route('/users', method=['POST'], strict_slashes=False)
def register_user() -> str:
    """POST/User
       Register user
       :Return Jonsinify Playload
    """
    email = request.form.get('email')
    password = request.form.get('password')

    try:
        user = AUTH.register_user(email, password)
        if user:
            return jsonify(
                {"email": user.email,
                 "message": "user created"}), 200
    except ValueError:
        return jsonify({"message":
                        "email already registered"}), 400
