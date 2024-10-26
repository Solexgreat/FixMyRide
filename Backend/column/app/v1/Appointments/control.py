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
            date_time = datetime.now()

        try:
            # Create a new appointment
            appointment = Appointment(date_time=date_time, customer_id=customer_id,
                                      service_id=service_id, model=model, status=status)
            self._session.add(appointment)
            self._session.commit()

            print("Created Appointment ID:", appointment.appointment_id)

        except Exception as e:
            self._session.rollback()
            print("Exception occurred:", e, type(e))
            raise Exception(f'{e}')
        return appointment

    def update_appointment(self, appointment_id: str, **kwargs: dict):
        """
            update appointment
        """
        #Fetech the appointment and check if it exist
        appointment = self._session.query(Appointment).get(appointment_id)
        if not appointment:
            raise NoResultFound (f'Appointment not found')

        #Update the appointment field with kwargs value
        for key, value in kwargs.items():
            setattr(appointment, key, value)

        #Update the updateed_date field
        appointment.updated_date = datetime.now()

        self._session.commit()


        return appointment

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