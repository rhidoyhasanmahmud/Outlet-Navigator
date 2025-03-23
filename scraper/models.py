from typing import List
from sqlalchemy import Column, Integer, String, Float
from database.db import Base

class OutletDB(Base):
    __tablename__ = 'outlets'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    address = Column(String)
    phone = Column(String)
    latitude = Column(Float)
    longitude = Column(Float)
    features = Column(String)
    waze_link = Column(String)

class Outlet:
    def __init__(self, name, address, phone, latitude, longitude, features, waze_link):
        self.name = name
        self.address = address
        self.phone = phone
        self.latitude = latitude
        self.longitude = longitude
        self.features = features
        self.waze_link = waze_link

    def to_dict(self):
        return self.__dict__