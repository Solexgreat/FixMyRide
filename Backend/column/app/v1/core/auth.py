from ..users.control import UserControl
from ..users.model import User
from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.orm.exc import NoResultFound
import bcrypt
from .security import _hash_password, SECURITY



class AUTH:
    """Auth class to interact with the authentication database.
    """
    def __init__(self) -> None:
        self._db = UserControl()

    def register_user(self,**kwargs) -> User:
        """Find user via there email info
           add_user and return new_user
        """
        try:
            user = self._db.find_user(**kwargs)
            if user:
               raise ValueError (f"{user.email} already exits")
        except NoResultFound:
            password = kwargs.get('password')
            if not password:
                raise ValueError("Password is required")
            hash_pwd = _hash_password(password)
            SECURITY.create_session(user.email)
            new_user = self._db.add_user(**kwargs, password=hash_pwd)
            return new_user


    def verify_login(self, **kwargs: dict) -> User:
        """Verify if the user logging details
           are valid
        """
        try:
            password = kwargs.get('password')
            user = self._db.find_user(**kwargs)
            password_encode = _hash_password(password)
            user_pwd = user.password
            if bcrypt.checkpw(user_pwd, password_encode):
                SECURITY.create_session(user.email)
                return user
            else:
                raise ValueError('Invalid password')
        except (NoResultFound, InvalidRequestError):
            raise Exception

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