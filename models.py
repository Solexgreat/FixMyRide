from sqlalchemy import Boolean, Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from flask_security import Security, SQLAlchemyUserDatastore, UserMixin, RoleMixin


Base = declarative_base()

 

class User(Base):
    __tablename__ = 'user'

    user_id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    email = Column(String(255), nullable=False)
    password = Column(String(255), nullable=False)
    session = Column(String(225))
    reset_token = Column(String(225))
    roles = Column(String, nullable=False)

class Service(Base):
    __tablename__ = 'service'

    service_id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    price = Column(Float, nullable=False)
    
class Appointment(Base):
    __tablename__ = 'appointment'

    appointment_id = Column(Integer, primary_key=True)
    date_time = Column(DateTime, nullable=False)
    customer_id = Column(Integer, ForeignKey('user.user_id'), nullable=False)
    service_id = Column(Integer, ForeignKey('service.service_id'), nullable=False)
    model = Column(String(50)),
    customer = relationship('User', foreign_keys=[customer_id])
    service = relationship('Service', foreign_keys=[service_id])

class Repair(Base):
    __tablename__ = 'repair'

    repair_id = Column(Integer, primary_key=True)
    date_time = Column(DateTime, nullable=False)
    mechanic_id = Column(Integer, ForeignKey('user.user_id'), nullable=False)
    customer_id = Column(Integer, ForeignKey('user.user_id'), nullable=False)
    service_id = Column(Integer, ForeignKey('service.service_id'), nullable=False)
    mechanic = relationship('User', foreign_keys=[mechanic_id])
    customer = relationship('User', foreign_keys=[customer_id])
    service = relationship('Service', foreign_keys=[service_id])

class Revenue(Base):
    __tablename__ = 'revenue'

    revenue_id = Column(Integer, primary_key=True)
    date = Column(DateTime, nullable=False)
    total_revenue = Column(Float, nullable=False)
    total_appointments = Column(Integer, nullable=False)
    total_repairs = Column(Integer, nullable=False)