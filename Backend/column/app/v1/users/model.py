from sqlalchemy import Boolean, Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.types import Enum
from sqlalchemy.orm import relationship
from .....db import Base
from ..Services.model import Service
# from flask_security import Security, SQLAlchemyUserDatastore, UserMixin, RoleMixin



class User(Base):
    __tablename__ = 'users'

    user_id = Column(Integer, primary_key=True)
    first_name = Column(String(255), nullable=False)
    last_name = Column(String(255), nullable=False)
    user_name = Column(String(255), nullable=False, unique=True)
    email = Column(String(255), nullable=False, unique=True)
    password = Column(String(255), nullable=False)
    session_id = Column(String(225), nullable=True)
    reset_token = Column(String(225), nullable=True)
    token_expiration = Column(DateTime(), nullable=True)
    session_expiration= Column(DateTime(), nullable=True)
    is_active = Column(Boolean(), default=True)
    role = Column(Enum('admin', 'mechanic', 'customer'), nullable=False)

    services = relationship("Service", back_populates="seller")
