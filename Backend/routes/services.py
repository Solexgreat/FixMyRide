from flask import Flask
from flask import Flask, jsonify, request, abort, redirect, render_template, flash
# from flask_login import login_user, logout_user, login_required, current_user, LoginManager
# from .db import DB
from ..column.app.v1.Services.control import ServiceControl
from Backend.column.app.v1.core.auth import AUTH
from . import service_bp
from ..column.app.v1.core.middleware import authenticate



DB = ServiceControl()
AUTH = AUTH()


@service_bp.route('/service', methods=['GET'], strict_slashes=False)
@authenticate
def get_service() -> str:
    """Return all service
    """
    user = request.user
    if user.role != 'admin':
        return jsonify({'msg': "Not authorized"}), 403

    return jsonify(DB.get_service()), 200


@service_bp.route('/service', methods=['POST'], strict_slashes=False)
@authenticate
def create_service() ->str:
    """POST /revenue
       Return: Jsonify status 200
    """
    data = request.get_json()
    user = request.user
    seller_id = user.user_id

    try:
        if not data:
            return jsonify({'msg': 'Expecting data'}), 400

        service = DB.add_service(**data, seller_id=seller_id)
        return jsonify({"message": "Service is Created"}), 201
    except Exception as e:
        err_msg = "can't create appointment: {}".format(e)
        return (f"{err_msg}")