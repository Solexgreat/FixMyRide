from flask import Blueprint

user_bp = Blueprint('users', __name__, url_prefix='/users')
auth_bp = Blueprint('users', __name__, url_prefix='/auths')
service_bp = Blueprint('tasks', __name__, url_prefix='/tasks')
revenue_bp = Blueprint('auths', __name__, url_prefix='/revenues')
repair_bp = Blueprint('auths', __name__, url_prefix='/repairs')
appointment_bp = Blueprint('auths', __name__, url_prefix='/appointments')

# Import the routes
from .users import *
from .services import *
from .repairs import *
from .revenues import *
from .appointments import *
from .auths import *