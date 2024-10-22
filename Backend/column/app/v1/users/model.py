from sqlalchemy import Boolean, Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from ..Services.model import Service
# from flask_security import Security, SQLAlchemyUserDatastore, UserMixin, RoleMixin


Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    user_id = Column(Integer, primary_key=True)
    first_name = Column(String(255), nullable=False)
    last_name = Column(String(255), nullable=False)
    user_name = Column(String(255), nullable=False, unique=True)
    email = Column(String(255), nullable=False, unique=True)
    password = Column(String(255), nullable=False)
    session_id = Column(String(225))
    reset_token = Column(String(225), nullable=True)
    token_expiration = Column(DateTime(), nullable=True)
    session_expiration= Column(DateTime(), nullable=True)
    is_active = Column(Boolean(), default=True)
    role = Column(String, nullable=False)

    # services = relationship("Service", back_populates="seller")
