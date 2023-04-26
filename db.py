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
from datetime import datetime
from models import Base
from flask_security import Security, SQLAlchemyUserDatastore, UserMixin, RoleMixin


class DB:
    """DB class
    """

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
    
    def get_users(self) -> dict:
        """Return dict of users
        """
        users = self._session.query(User).all()
        return [u.__dict__ for u in users]
    
    def get_service(self) -> dict:
        """Return dict of services
        """
        services = self._session.query(Service).all()
        return [s.__dict__ for s in services]
    
    def get_all_appointment(self) -> dict:
        """Return dict of services
        """
        appointment = self._session.query(Appointment).all()
        return [a.__dict__ for a in appointment]
    
    def get_all_repairs(self) -> dict:
        """Return dict of services
        """
        repairs = self._session.query(Repair).all()
        return [r.__dict__ for r in repairs]
    
    def get_all_revenue(self) ->Revenue:
        """Add User to session
        """
        revenues = self._session.query(Revenue).all()

        return [r.__dict__ for r in revenues]
    
    def add_user(self, email: str, hashed_password: str, name: str, role: str) -> User:
        """Add User to session
        """
        user = User(email=email, password=hashed_password, name=name, role=role)
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
    
    def get_user_id(self, **kwargs) -> int:
        """To get the user_id """
        try:
            user = self.find_user(**kwargs)
            user_id = user.user_id
        except Exception as e:
            return e
        return user_id
    
    def get_service_id(self, **kwargs) -> int:
        """ """
        try:
            service = self._session.query(Service).filter_by(**kwargs).first()
            service_id = service.service_id
        except TypeError:
            return InvalidRequestError
        if service_id is None:
            return NoResultFound
        return service_id
        
    
    def add_appiontment(self, date_time: datetime, customer_id: int, service_id: int, model: str) -> Appointment:
        """Return list of Obj
        """
        appointment = Appointment(date_time=date_time, customer_id=customer_id,
                                  service_id=service_id, model=model)
        self._session.add(appointment)
        self._session.commit()
        revenue = self._session.query(Revenue).order_by(Revenue.date.desc()).first()
        if revenue:
            revenue.total_appointments += 1
        else:
            revenue = Revenue(date_time=date_time, total_appointments=1,
                          total_repair=0, total_revenue=0)   

        service = self._session.query(Service).get(service_id)
        if service:
            revenue.total_revenue += service.price
            if service.category == 'Repairs':
                revenue.total_repairs += 1
        
        self._session.add(revenue)
        self._session.commit()
 
    def add_repair(self, date_time: datetime.now(), customer_id: str, 
                        service_id: int, mechanic_id: int) -> Repair:
        """Return list of Obj
        """
        repairs = Repair(date_time=date_time,
                                customer_id=customer_id,
                                service_id=service_id, mechanic_id=mechanic_id)
        self._session.add(repairs)
        self._session.commit() 
        return repairs
    
    def add_revenue(self, date_time: datetime.now(), total_appointment: int, 
                        total_repair: int, total_revenue: int) -> Repair:
        """Return list of Obj
        """
        revenue = Repair(date_time=date_time, total_appointment=total_appointment, 
                        total_repair=total_repair, total_revenue=total_revenue)
        self._session.add(revenue)
        self._session.commit() 
        return revenue
    
    def add_service(self, name: str, price: int, category: str) -> dict:
        """Return dict of services
        """
        services = Service(name=name, price=price, category=category)
        self._session.add(services)
        self._session.commit()

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
