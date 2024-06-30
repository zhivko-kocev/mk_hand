from sqlalchemy import Column, Integer, String, Date
from .base import Base


class Lawyer(Base):
    __tablename__ = 'lawyer'
    id = Column(Integer, primary_key=True)
    name_surname = Column(String)
    telephone = Column(String)
    email = Column(String)
    date_zapishuvanje = Column(Date)
    registry_number = Column(Integer)
    number_upis = Column(Integer)
    date_upis = Column(Date)
    number_removal = Column(String)
    date_removal = Column(Date)
    geo_length = Column(Integer)
    geo_width = Column(Integer)
