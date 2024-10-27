from sqlalchemy import Boolean, Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
# from flask_security import Security, SQLAlchemyUserDatastore, UserMixin, RoleMixin
from .....db import Base


class Revenue(Base):
    __tablename__ = 'revenue'

    revenue_id = Column(Integer, primary_key=True)
    total_revenue = Column(Float, nullable=True, default=0)
    total_appointments = Column(Integer, nullable=True, default=0)
    total_repairs = Column(Integer, nullable=True, default=0)
    date_time = Column(DateTime, nullable=False)