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
from .....db import DB



def get_all_appointment() -> dict:
	"""Return dict of services
	"""
	appointment = DB._session.query(Appointment).all()
	return [a.__dict__ for a in appointment]


def add_appiontment( date_time: datetime, customer_id: int, service_id: int, model: str) -> Appointment:
	"""Return list of Obj
	"""
	appointment = Appointment(date_time=date_time, customer_id=customer_id,
														service_id=service_id, model=model)
	DB._session.add(appointment)
	DB._session.commit()
	revenue = DB._session.query(Revenue).order_by(Revenue.date.desc()).first()
	if revenue:
			revenue.total_appointments += 1
	else:
			revenue = Revenue(date_time=date_time, total_appointments=1,
										total_repair=0, total_revenue=0)

	service = DB._session.query(Service).get(service_id)
	if service:
			revenue.total_revenue += service.price
			if service.category == 'Repairs':
					revenue.total_repairs += 1

	DB._session.add(revenue)
	DB._session.commit()