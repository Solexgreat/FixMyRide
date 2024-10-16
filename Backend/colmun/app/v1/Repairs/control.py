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


def get_all_repairs() -> dict:
        """Return dict of services
        """
        repairs = DB._session.query(Repair).all()
        return [r.__dict__ for r in repairs]

def add_repair(date_time: datetime.now(), customer_id: str,
                        service_id: int, mechanic_id: int) -> Repair:
        """Return list of Obj
        """
        repairs = Repair(date_time=date_time,
                                customer_id=customer_id,
                                service_id=service_id, mechanic_id=mechanic_id)
        DB._session.add(repairs)
        DB._session.commit() 
        return repairs