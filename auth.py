from db import DB
from models import User, Appointment, Service, Repair, Revenue
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import InvalidRequestError
import uuid
import bcrypt

def _hash_password(password: str) -> bytes:
    """returned bytes is a salted hash of the input password
    """
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed

def _generate_uuid():
    """Generate and return
       string uuid
    """
    return str(uuid.uuid4())

class AUTH:
    """Auth class to interact with the authentication database.
    """
    def __init__(self) -> None:
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """
        """
        