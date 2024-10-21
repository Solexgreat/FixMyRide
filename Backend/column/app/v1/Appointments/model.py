from sqlalchemy import Boolean, Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
# from flask_security import Security, SQLAlchemyUserDatastore, UserMixin, RoleMixin


Base = declarative_base()


class Appointment(Base):
    __tablename__ = 'appointment'

    appointment_id = Column(Integer, primary_key=True)
    date_time = Column(DateTime, nullable=False)
    customer_id = Column(Integer, ForeignKey('user.user_id'), nullable=False)
    service_id = Column(Integer, ForeignKey('service.service_id'), nullable=False)
    model = Column(String(50))
    status = Column(String(50), default='pending')
    updated_date = Column(DateTime, nullable=False)
    customer = relationship('User', foreign_keys=[customer_id])
    service = relationship('Service', foreign_keys=[service_id])