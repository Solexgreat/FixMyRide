from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import InvalidRequestError
from Backend.models import User, Appointment, Service, Repair, Revenue
from typing import List
from datetime import datetime
from .....db import DB


def get_service() -> dict:
	"""Return dict of services
	"""
	services = DB._session.query(Service).all()
	return [s.__dict__ for s in services]

def get_service_id( **kwargs) -> int:
	""" """
	try:
			service = DB._session.query(Service).filter_by(**kwargs).first()
			service_id = service.service_id
	except TypeError:
			return InvalidRequestError
	if service_id is None:
			return NoResultFound
	return service_id

def add_service(name: str, price: int, category: str) -> dict:
	"""Return dict of services
	"""
	services = Service(name=name, price=price, category=category)
	DB._session.add(services)
	DB._session.commit()