from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import InvalidRequestError
from sqlalchemy import and_
from .model import Appointment
from typing import List
from datetime import datetime
from .....db import DB
from ..Revenues.model import Revenue
from ..Services.model import Service


class AppointmentControl(DB):
    """Appointment control class that inherits from DB"""

    def get_all_appointments(self, customer_id: int) -> dict:
        """Return a list of all appointments as dictionaries"""

        appointments = self._session.query(Appointment).filter_by(customer_id=customer_id).all()
        return [a.__dict__ for a in appointments]

    def add_appointment(self, date_time: datetime, customer_id: int, service_id: int, model: str, status: str) -> Appointment:
        """Add an appointment and update revenue"""

        if date_time is None:
            date_time = date_time.date()

        try:
            # Create a new appointment
            appointment = Appointment(date_time=date_time, customer_id=customer_id,
                                      service_id=service_id, model=model, status=status)
            self._session.add(appointment)
            self._session.commit()

        except Exception as e:
            self._session.rollback()
            raise e

    def update_appointment(self, status: str, appointment_id: str):
        """
            update appointment
        """
        appointments = self._session.query(Appointment).get(appointment_id)

        if not appointments:
            raise NoResultFound (f'Appointment not found')

        appointments = self._session.query(Appointment).filter_by(appointment_id=appointment_id).update(status=status,
                                                                                                        updated_date=datetime.now())

    def get_appointment_between_dates(self, start_date: datetime, end_date: datetime):
        """
        """
        appointments = self._session.query(Appointment).filter(
            Appointment.date_time.between(start_date, end_date)
        ).all()
        return appointments

    def get_completed_appointment_between_dates(self, start_date: datetime, end_date: datetime):
        """
        """
        appointments = self._session.query(Appointment).filter(
            and_(
                Appointment.status == 'completed',
                Appointment.updated_date.between(start_date, end_date)
            )
            ).all()
        return appointments