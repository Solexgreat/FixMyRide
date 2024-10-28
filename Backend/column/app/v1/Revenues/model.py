from sqlalchemy import Boolean, Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
# from flask_security import Security, SQLAlchemyUserDatastore, UserMixin, RoleMixin
from datetime import datetime
from .....db import Base


class Revenue(Base):
    __tablename__ = 'revenue'

    revenue_id = Column(Integer, primary_key=True)
    total_revenue = Column(Float, nullable=True, default=0.00)
    total_appointments = Column(Integer, nullable=True, default=0)
    total_repairs = Column(Integer, nullable=True, default=0)
    date_time = Column(DateTime, nullable=False, default=datetime.now().date())


    def to_dict(self):
        return {
            'date': self.date_time,
            'revenue_id': self.revenue_id,
            'total_revenue': self.total_revenue,
            'total_appointments': self.total_appointments,
            'total_repairs': self.total_repairs
        }