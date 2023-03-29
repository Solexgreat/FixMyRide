"""DB module
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import InvalidRequestError
from models import User, Appointment, Service, Repair, Revenue
from typing import List

from models import Base


class DB:
    """DB class
    """
    listOfCls = [User, Appointment, Service, Repair, Revenue]

    def __init__(self) -> None:
        """Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///FMR.db", echo=True)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object
        """
        if self.__session is None:
            DBsession = sessionmaker(bind=self._engine)
            self.__session = DBsession()
        return self.__session
    
    def add_user(self, email: str, hashed_password: str) -> User:
        """Add User to session
        """
        user = User(email=email, password=hashed_password)
        self._session.add(user)
        self._session.commit()
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
    
    def add_appiontment(self, date_time: str,customer_id: str, 
                        service_id: str) -> Appointment:
        """Return list of Obj
        """
        appointment = Appointment(date_time=date_time,
                                customer_id=customer_id,
                                service_id=service_id,)
        self._session.add(appointment)
        self._session.commit() 
        return appointment
    
    def add_repair(self, date_time: str,customer_id: str, 
                        service_id: str, mechanic_id: str) -> Repair:
        """Return list of Obj
        """
        repairs = Repair(date_time=date_time,
                                customer_id=customer_id,
                                service_id=service_id, mechanic_id=mechanic_id)
        self._session.add(repairs)
        self._session.commit() 
        return repairs

    
