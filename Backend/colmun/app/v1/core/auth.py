from db import DB
from Backend.models import User, Appointment, Service, Repair, Revenue
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import InvalidRequestError
import uuid
import bcrypt
from .security import _hash_password



class AUTH:
    """Auth class to interact with the authentication database.
    """
    def __init__(self) -> None:
        self._db = DB()

    def register_user(self, email: str, password: str, name: str, role: str) -> User:
        """Find user via there email info
           add_user and return new_user
        """
        try:
            user = self._db.find_user(email=email)
            if user:
               raise ValueError (f"{user.name} already exits")
        except:
            hash_pwd = _hash_password(password)
            new_user = self._db.add_user(email, hash_pwd, name, role)
            return new_user


    def verify_login(self, email, password):
        """Verify if the user logging details
           are valid
        """
        try:
            user = self._db.find_user(email=email)
            password_encode = password.encode('utf-8')
            user_pwd = user.password
            return bcrypt.checkpw(user_pwd, password_encode)
        except (NoResultFound, InvalidRequestError):
            return False

    def get_current_user(self, session_id: str) -> User:
        """get the user from  the session_id
        """
        if not session_id:
            return None
        try:
            user = self._db.find_user(session_id)
            return user
        except NoResultFound:
            return None

    def update_password(self, reset_token: str, password: str) -> None:
        """Find the user by reset_token
           update the password
        """
        if reset_token is None:
            return None
        try:
            user = self._db.find_user(reset_token=reset_token)
        except NoResultFound:
            raise ValueError
        hashed_pwd = _hash_password(password)
        self._db.update_user(user.user_id, password=hashed_pwd)
        user.reset_token = None