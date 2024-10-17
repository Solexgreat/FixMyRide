from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import InvalidRequestError
from .model import Service
from typing import List
from datetime import datetime
from .....db import DB


class ServiceControl(DB):
    """Service control class that inherits from DB"""

    def get_service(self) -> dict:
        """Return a list of services as dictionaries"""
        services = self._session.query(Service).all()
        return [s.__dict__ for s in services]

    def get_service_id(self, **kwargs) -> int:
        """Get the service ID based on provided criteria"""
        try:
            service = self._session.query(Service).filter_by(**kwargs).first()
            if service is None:
                raise NoResultFound(f"No service found with criteria: {kwargs}")
            service_id = service.service_id
        except TypeError:
            raise InvalidRequestError("Invalid arguments provided.")
        return service_id

    def add_service(self, name: str, price: int, category: str) -> dict:
        """Add a service to the session and commit"""
        try:
            service = Service(name=name, price=price, category=category)
            self._session.add(service)
            self._session.commit()
        except Exception as e:
            self._session.rollback()
            raise e
        return service