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

    def get_all_appointments(self, user_id: int, role: str) -> dict:
        """Return a list of all appointments as dictionaries"""

        try:

            if role == 'admin':
                appointments = self._session.query(Appointment).all()
            elif role == 'mechanic':
                appointments = self._session.query(Appointment).filter_by(mechanic_id=user_id).all()
            else:
                appointments = self._session.query(Appointment).filter_by(mechanic_id=customer_id).all()

            return [a.to_dict() for a in appointments]
        except Exception as e:
            raise(f'{e}')

    def get_appointments(self, appointment_id: int, user_id: int, role: str) -> dict:
        """Return a list of all appointments as dictionaries"""
        #Get appointment and verify if it exist
        appointment = self._session.query(Appointment).filter_by(appointment_id=appointment_id).first()
        if not appointment:
            raise NoResultFound(f'Appointment with {appointment_id} does not exist')
        try:
            if role == 'admin':
                return appointment.to_dict()

            #Get the mechanic_id and check if it exist
            mechanic_id = appointment.mechanic_id
            if not mechanic_id:
                raise NoResultFound(f'Service or Mechanic no longer available')

            #Check if the user(mechanic or customer) is authorize to get appointment
            customer_id = appointment.customer_id
            if user_id != mechanic_id or user_id != customer_id:
                raise InvalidRequestError(f'Unauthorized request')

            return appointment.to_dict()
        except Exception as e:
            raise (f'{e}')

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

        #Update the updated_date field
        appointment.updated_date = datetime.now()

        self._session.commit()


        return appointment

    def get_appointment_between_dates(self, start_date: datetime, end_date: datetime):
        """
            Get appointments between a period of time
        """
        appointments = self._session.query(Appointment).filter(
            Appointment.date_time.between(start_date, end_date)
        ).all()
        return appointments

    def get_completed_appointment_between_dates(self, start_date: datetime, end_date: datetime):
        """
            Get appointments with 'status' complete between a period of time
        """
        appointments = self._session.query(Appointment).filter(
            and_(
                Appointment.status == 'completed',
                Appointment.updated_date.between(start_date, end_date)
            )
            ).all()
        return appointments