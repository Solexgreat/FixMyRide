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
            new_user = self._db.add_user(email, password, name, role)
            return new_user
    
    def valid_loggin(self, email, password):
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
        
    def create_session(self, email: str,):
        """Create a session via uuid
           update the user session and 
           retyrb the session id 
        """
        try:
            user = self._db.find_user(email=email)
            session_id = uuid.uuid4()
            user_id = user.user_id
            user = self._db.update_user(user_id, session_id=session_id)
            return session_id
        except NoResultFound:
            return None
        
    def get_user_from_session_id(self, session_id: str) -> User:
        """get the user from  the session_id
        """
        if not session_id:
            return None
        try:
            user = self._db.find_user(session_id)
            return user
        except NoResultFound:
            return None
        
    def destroy_session(self, user_id: int) -> None:
        """Updates user's session_id to None
        """
        if not user_id:
            return None
        try:
            user = self._db.find_user(user_id)
            session_id = None
            self._db.update_user(user_id, session_id=session_id)
        except NoResultFound:
            return None

    def get_reset_password_token(self, email: str) -> str:
        """Generate new token with uuid4
        """
        try:
            user = self._db.find_user(email=email)
        except NoResultFound:
            raise ValueError

        reset_token = _generate_uuid()
        self._db.update_user(user.user_id, reset_token=reset_token)
        return reset_token

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

