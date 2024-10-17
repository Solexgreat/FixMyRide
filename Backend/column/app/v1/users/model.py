from sqlalchemy import Boolean, Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
# from flask_security import Security, SQLAlchemyUserDatastore, UserMixin, RoleMixin


Base = declarative_base()


class User(Base):
    __tablename__ = 'user'

    user_id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    email = Column(String(255), nullable=False)
    password = Column(String(255), nullable=False)
    session = Column(String(225))
    reset_token = Column(String(225), nullable=True)
    token_expiration = Column(DateTime(), nullable=True)
    is_active = Column(Boolean(), default=True)
    role = Column(String, nullable=False)