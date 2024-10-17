from ..users.control import UserControl
from ..users.model import User
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


class SECURITY:
    """Auth class to interact with the authentication database.
    """
    def __init__(self) -> None:
        self._db = UserControl()

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