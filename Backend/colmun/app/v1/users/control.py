from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import InvalidRequestError
from Backend.models import User, Appointment, Service, Repair, Revenue
from typing import List
from datetime import datetime
from Backend.models import Base



 def get_users(self) -> dict:
        """Return dict of users
        """
        users = self._session.query(User).all()
        return [u.__dict__ for u in users]

 def add_user(self, email: str, hashed_password: str, name: str, role: str) -> User:
        """Add User to session
        """
        try:
            user = User(email=email, password=hashed_password, name=name, role=role)
            self._session.add(user)
            self._session.commit()
        except Exception as e:
            self._session.rollback()
        return user

def find_user(self, **kwargs) -> User:
        """ find user by email
            and return user
        """
        try:
            user = self._session.query(User).filter_by(**kwargs).first()
        except TypeError:
            raise InvalidRequestError
        if user is None:
            raise NoResultFound
        return user

    def get_user_id(self, **kwargs) -> int:
        """To get the user_id """
        try:
            user = self.find_user(**kwargs)
            user_id = user.user_id
        except Exception as e:
            return e
        return user_id

def update_user(self, user_id: int, **kwargs) -> None:
        """
        """
        try:
            user = self.find_user(user_id=user_id)
            for i, j in kwargs.items():
                if hasattr(user, i):
                    setattr(user, i, j)
                else:
                    raise ValueError(f"{i} is not a valid attribute of User")
        except NoResultFound:
            return (f"Invalid user_id")
        return None
