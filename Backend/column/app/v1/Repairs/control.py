from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import InvalidRequestError
from .model import Repair
from ..Services.model import Service
from ..Revenues.model import Revenue
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
            repair = Repair(date_time=datetime.now(),
                            customer_id=customer_id,
                            service_id=service_id,
                            mechanic_id=mechanic_id)
            self._session.add(repair)
            self._session.commit()

            #Update revenue
            revenue = self._session.query(Revenue).order_by(Revenue.date.desc()).first()
            # if revenue:
            #     revenue.total_appointments += 1
            # else:
            #     revenue = Revenue(date_time=date_time, total_appointments=1,
            #                       total_repairs=0, total_revenue=0)

            # Update revenue based on the service
            service = self._session.query(Service).get(service_id)
            if service:
                revenue.total_revenue += service.price
                if service.category == 'Repairs':
                    revenue.total_repairs += 1

            self._session.add(revenue)
            self._session.commit()
            return repair

        except Exception as e:
            self._session.rollback()
            raise e  # Raise the exception after rolling back