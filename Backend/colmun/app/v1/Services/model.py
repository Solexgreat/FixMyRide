from sqlalchemy import Boolean, Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from flask_security import Security, SQLAlchemyUserDatastore, UserMixin, RoleMixin


Base = declarative_base()

class Service(Base):
    __tablename__ = 'service'

    service_id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    price = Column(Float, nullable=False)