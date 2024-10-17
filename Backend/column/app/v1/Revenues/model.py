from sqlalchemy import Boolean, Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from flask_security import Security, SQLAlchemyUserDatastore, UserMixin, RoleMixin


Base = declarative_base()


class Revenue(Base):
    __tablename__ = 'revenue'

    revenue_id = Column(Integer, primary_key=True)
    date = Column(DateTime, nullable=False)
    total_revenue = Column(Float, nullable=False)
    total_appointments = Column(Integer, nullable=False)
    total_repairs = Column(Integer, nullable=False)