from sqlalchemy import Boolean, Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from flask_security import Security, SQLAlchemyUserDatastore, UserMixin, RoleMixin


Base = declarative_base()

class Role(Base, RoleMixin):
    __tablename__ = 'roles'

    role_id = Column(Integer, primary_key=True)
    name = Column(String(80), nullable=False)
    description = Column(String(255))

class User_roles(Base):
    __tablename__ = 'User_roles'

    user_roles_id = Column(Integer, primary_key=True)
    user_id = Column('user.id', Integer, ForeignKey('User.user_id'))
    role_id = Column('role_id', Integer, ForeignKey('Role.role_id'))

class User(Base, UserMixin):
    __tablename__ = 'user'

    user_id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    email = Column(String(255), nullable=False)
    password = Column(String(255), nullable=False)
    session = Column(String(225))
    reset_token = Column(String(225))
    active = Column(Boolean())
    confirm = Column(DateTime())
    roles = relationship('Role', secondary='User', backref='users')

class Service(Base):
    __tablename__ = 'service'

    service_id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    category = Column(String(255), nullable=False)
    price = Column(Float, nullable=False)
    

class Appointment(Base):
    __tablename__ = 'appointment'

    appointment_id = Column(Integer, primary_key=True)
    date_time = Column(DateTime, nullable=False)
    customer_id = Column(Integer, ForeignKey('user.user_id'), nullable=False)
    service_id = Column(Integer, ForeignKey('service.service_id'), nullable=False)
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