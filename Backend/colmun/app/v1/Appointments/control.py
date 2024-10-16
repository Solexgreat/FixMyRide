from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import InvalidRequestError
from .model import Appointment
from typing import List
from datetime import datetime
from .....db import DB
from ..Revenues.model import Revenue


class AppointmentControl(DB):
    """Appointment control class that inherits from DB"""

    def get_all_appointments(self) -> dict:
        """Return a list of all appointments as dictionaries"""
        appointments = self._session.query(Appointment).all()
        return [a.__dict__ for a in appointments]

    def add_appointment(self, date_time: datetime, customer_id: int, service_id: int, model: str) -> Appointment:
        """Add an appointment and update revenue"""
        try:
            # Create a new appointment
            appointment = Appointment(date_time=date_time, customer_id=customer_id,
                                      service_id=service_id, model=model)
            self._session.add(appointment)
            self._session.commit()

            # Update revenue
            revenue = self._session.query(Revenue).order_by(Revenue.date.desc()).first()
            if revenue:
                revenue.total_appointments += 1
            else:
                revenue = Revenue(date_time=date_time, total_appointments=1,
                                  total_repairs=0, total_revenue=0)

            # Update revenue based on the service
            service = self._session.query(Service).get(service_id)
            if service:
                revenue.total_revenue += service.price
                if service.category == 'Repairs':
                    revenue.total_repairs += 1

            self._session.add(revenue)
            self._session.commit()
            return appointment

        except Exception as e:
            self._session.rollback()
            raise e