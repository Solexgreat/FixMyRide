from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import InvalidRequestError
from .model import Revenue
from typing import List
from datetime import datetime
from .....db import DB


class RevenueControl(DB):
    """Revenue control class that inherits from DB"""
    def get_all_revenue(self) -> list:
        """Retrieve all revenue records from the database."""
        revenues = self._session.query(Revenue).all()
        return [r.__dict__ for r in revenues]

    def add_revenue(self, date_time: datetime, total_appointment: int,
                    total_repair: int, total_revenue: int) -> Revenue:
        """Add a new revenue record to the session and commit it."""
        revenue = Revenue(date_time=date_time, total_appointment=total_appointment,
                          total_repair=total_repair, total_revenue=total_revenue)
        self._session.add(revenue)
        self._session.commit()
        return revenue