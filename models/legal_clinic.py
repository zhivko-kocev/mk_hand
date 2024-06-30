from sqlalchemy import Column, Integer, String, Date
from .base import Base


class LegalClinic(Base):
    __tablename__ = 'legal_clinic'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    address = Column(String)
    telephone = Column(String)
    email = Column(String)
    mentor = Column(String)
    solution_number = Column(String)
    date_solution = Column(Date)
    geo_length = Column(Integer)
    geo_width = Column(Integer)
