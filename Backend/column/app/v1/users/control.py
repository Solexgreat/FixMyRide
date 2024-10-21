from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import InvalidRequestError
from .model import User
from typing import List
from datetime import datetime
from .....db import DB



class UserControl(DB):
    """User control class that inherits from DB"""

    def get_users(self) -> dict:
        """Return a list of users as dictionaries"""
        users = self._session.query(User).all()
        return [u.__dict__ for u in users]

    def add_user(self, **kwargs) -> User:
        """Add a user to the session and commit"""
        try:
            user = User(**kwargs)
            self._session.add(user)
            self._session.commit()
        except Exception as e:
            self._session.rollback()
            raise e
        return user

    def find_user(self, **kwargs) -> User:
        """Find a user by provided criteria (e.g., email) and return the user"""
        try:
            user_name = kwargs.get('user_name')
            email= kwargs.get('email')
            if email:
                user = self._session.query(User).filter_by(email=email).first()
            elif user_name:
                user = self._session.query(User).filter_by(user_name=user_name).first()
            else:
                raise ValueError("No search criteria provided")
        except TypeError:
            raise InvalidRequestError
        if user is None:
            raise NoResultFound
        return user

    def get_user_id(self, **kwargs) -> int:
        """Get the user_id of a user based on given criteria"""
        try:
            user = self.find_user(**kwargs)
            user_id = user.user_id
        except Exception as e:
            return e
        return user_id

    def update_user(self, **kwargs: dict) -> None:
        """Update a user's attributes"""
        try:
            user = self.find_user(**kwargs)
            for key, value in kwargs.items():
                if hasattr(user, key):
                    setattr(user, key, value)
                else:
                    raise ValueError(f"{key} is not a valid attribute of User")
            self._session.commit()
        except NoResultFound:
            return NoResultFound
        return None

    def find_user_by_session_id(self, session_id: str):
        """
            Get user via session_id
        """
        user = self._session.query(User).filter_by(session_id=session_id).first()
        return user