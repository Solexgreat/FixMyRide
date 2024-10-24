from sqlalchemy import Boolean, Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from .....db import Base
# from flask_security import Security, SQLAlchemyUserDatastore, UserMixin, RoleMixin




class Service(Base):
    __tablename__ = 'service'

    service_id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    price = Column(Float, nullable=False)
    category = Column(String(255), nullable=False)
    seller_id = Column(Integer, ForeignKey('users.user_id'), nullable=False)

    seller = relationship("User", back_populates="services")