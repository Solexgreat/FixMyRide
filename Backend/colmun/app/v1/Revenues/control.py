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


def get_all_revenue() ->Revenue:
	"""Add User to session
	"""
	revenues = DB._session.query(Revenue).all()

	return [r.__dict__ for r in revenues]


def add_revenue(date_time: datetime.now(), total_appointment: int,
									total_repair: int, total_revenue: int) -> Repair:
	"""Return list of Obj
	"""
	revenue = Repair(date_time=date_time, total_appointment=total_appointment,
									total_repair=total_repair, total_revenue=total_revenue)
	DB._session.add(revenue)
	DB._session.commit()
	return revenue