from ..users.control import UserControl, logger
from ..users.model import User
from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.orm.exc import NoResultFound
import bcrypt
from datetime import datetime, timedelta
from .security import _hash_password, SECURITY

DB = UserControl()
security = SECURITY()



class AUTH:
    """Auth class to interact with the authentication database.
    """
    def __init__(self) -> None:
        self._db = DB

    def register_user(self, **kwargs) -> User:
        """Find user via there email info
           add_user and return new_user
        """
        try:
            user = self._db.find_user(**kwargs)
            if user:
               raise ValueError (f"user already exits {user}")
        except NoResultFound:
            password = kwargs.get('password')
            if not password:
                raise ValueError("Password is required")
            hash_pwd = _hash_password(password)
            session_expiration = datetime.now() + timedelta(hours=24)
            session_id = security.create_session()
            kwargs.pop('password', None)

            new_user = self._db.add_user(**kwargs, password=hash_pwd, session_expiration=session_expiration, session_id=session_id)

            return new_user


    def verify_login(self, **kwargs: dict) -> User:
        """Verify if the user logging details
           are valid
        """
        user_name = kwargs.get('user_name')
        email = kwargs.get('email')

        if not email and not user_name:
            raise ValueError("No search criteria provided")

        try:
            password = kwargs.get('password')

            if user_name:
                user = self._db.find_user('user_name', user_name)
            if not user_name:
                user = self._db.find_user('email', email)
            user_pwd = user.password


            if bcrypt.checkpw(password.encode('utf-8'), user_pwd.encode('utf-8')):
                session_id = security.create_session()
                user = self._db.update_user(**kwargs, session_id=session_id)
                return user
            else:
                raise ValueError('Invalid password')
        except (InvalidRequestError) as e:
            logger.exception("Database error:", exc_info=e)
            raise Exception(f'{e}')

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