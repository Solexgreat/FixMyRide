from sqlalchemy import Boolean, Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from .....db import Base
# from flask_security import Security, SQLAlchemyUserDatastore, UserMixin, RoleMixin



class Repair(Base):
    __tablename__ = 'repair'

    repair_id = Column(Integer, primary_key=True)
    mechanic_id = Column(Integer, ForeignKey('users.user_id'), nullable=False)
    customer_id = Column(Integer, ForeignKey('users.user_id'), nullable=False)
    service_id = Column(Integer, ForeignKey('service.service_id'), nullable=False)
    date_time = Column(DateTime, nullable=False)

    mechanic = relationship('User', foreign_keys=[mechanic_id], primaryjoin="Repair.mechanic_id == User.user_id")
    customer = relationship('User', foreign_keys=[customer_id], primaryjoin="Repair.customer_id == User.user_id")
    service = relationship('Service', foreign_keys=[service_id])

    def to_dict(self):
        return {
            'date': self.date_time,
            'repair_id': self.repair_id,
            'customer_id': self.customer_id,
            'service_id': self.service_id,
            'mechanic_id': self.mechanic_id
        }