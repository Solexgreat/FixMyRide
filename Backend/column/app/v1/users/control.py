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

    def add_user(self, email: str, hashed_password: str, name: str, role: str) -> User:
        """Add a user to the session and commit"""
        try:
            user = User(email=email, password=hashed_password, name=name, role=role)
            self._session.add(user)
            self._session.commit()
        except Exception as e:
            self._session.rollback()
            raise e
        return user

    def find_user(self, **kwargs) -> User:
        """Find a user by provided criteria (e.g., email) and return the user"""
        try:
            user = self._session.query(User).filter_by(**kwargs).first()
        except TypeError:
            raise InvalidRequestError("Invalid arguments provided.")
        if user is None:
            raise NoResultFound(f"No user found with criteria: {kwargs}")
        return user

    def get_user_id(self, **kwargs) -> int:
        """Get the user_id of a user based on given criteria"""
        try:
            user = self.find_user(**kwargs)
            user_id = user.user_id
        except Exception as e:
            return e
        return user_id

    def update_user(self, user_id: int, **kwargs) -> None:
        """Update a user's attributes"""
        try:
            user = self.find_user(user_id=user_id)
            for key, value in kwargs.items():
                if hasattr(user, key):
                    setattr(user, key, value)
                else:
                    raise ValueError(f"{key} is not a valid attribute of User")
            self._session.commit()
        except NoResultFound:
            return f"Invalid user_id"
        return None