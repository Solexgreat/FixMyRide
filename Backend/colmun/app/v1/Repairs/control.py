from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import InvalidRequestError
from .model import Repair
from typing import List
from datetime import datetime
from .....db import DB


class RepairControl(DB):
    """Repair control class that inherits from DB"""

    def get_all_repairs(self) -> dict:
        """Return a list of all repairs as dictionaries"""
        repairs = self._session.query(Repair).all()
        return [r.__dict__ for r in repairs]

    def add_repair(self, date_time: datetime = None, customer_id: str = '',
                   service_id: int = 0, mechanic_id: int = 0) -> Repair:
        """Add a new repair to the database and return the repair object"""
        if date_time is None:
            date_time = datetime.now()  # Use current time if not provided
        try:
            repair = Repair(date_time=date_time,
                            customer_id=customer_id,
                            service_id=service_id,
                            mechanic_id=mechanic_id)
            self._session.add(repair)
            self._session.commit()
        except Exception as e:
            self._session.rollback()
            raise e  # Raise the exception after rolling back
        return repair