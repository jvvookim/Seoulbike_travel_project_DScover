from unicodedata import category
from sqlalchemy import Column, Integer, String, Float
from pydantic import BaseModel
from database import BASE

class TravelTable(BASE):
    __tablename__ = "travel"
    id = Column(Integer, primary_key=True, autoincrement=True)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    nearest = Column(String, nullable=False)
    rank = Column(Integer, nullable=False)
    category = Column(String, nullable=False)
    time = Column(Float, nullable=True)
    name = Column(String(120), nullable=False)

class Travel(BaseModel):
    id: int
    latitude: float
    longitude: float
    nearest: str
    rank: int
    category: str
    time: float
    name: str

class RestTable(BASE):
    __tablename__ = "rest"
    id = Column(Integer, primary_key=True, autoincrement=True)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    category = Column(String, nullable=False)
    name = Column(String, nullable=False)
    nearest = Column(String, nullable=False)
    rank = Column(Integer, nullable=False)

class Rest(BaseModel):
    id: int
    latitude: float
    longitude: float
    category: str
    name: str
    nearest: str
    rank: int

class CafeTable(BASE):
    __tablename__ = "cafe"
    id = Column(Integer, primary_key=True, autoincrement=True)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    category = Column(String, nullable=False)
    name = Column(String, nullable=False)
    nearest = Column(String, nullable=False)
    rank = Column(Integer, nullable=False)

class Cafe(BaseModel):
    id: int
    latitude: float
    longitude: float
    category: str
    name: str
    nearest: str
    rank: int

class Input(BaseModel):
    id: list
    latitude: float
    longitude: float