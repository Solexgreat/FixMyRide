from flask import Flask
from flask_jwt_extended import JWTManager
from .config import Config
from .routes import user_bp, service_bp, appointment_bp, repair_bp, revenue_bp, auth_bp  # Import your blueprints
from .column.app.v1.error import register_error_handlers  # Import error handlers
from .db import DB  # Import your DB class


def create_app():
    app = Flask(__name__)

    # Load configuration from config class
    app.config.from_object(Config)

    # Configure your secret key for encoding JWT
    app.config['JWT_SECRET_KEY'] = app.config.get('JWT_SECRET')

    # Initialize JWT manager
    jwt = JWTManager(app)

    # Initialize the database and attach it to the app
    db = DB()
    app.db = db

    # Register your blueprints (routes)
    app.register_blueprint(user_bp)
    app.register_blueprint(service_bp)
    app.register_blueprint(revenue_bp)
    app.register_blueprint(repair_bp)
    app.register_blueprint(appointment_bp)

    # Register error handlers
    register_error_handlers(app)

    return app