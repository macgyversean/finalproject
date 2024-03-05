from sqlalchemy import Column, Integer, String, Text, ForeignKey
from pydantic import BaseModel
from db import engine 
from models.Base import Base

class Users(Base):
    __tablename__ = 'USERS'
    id = Column(Integer, primary_key=True,)
    Name = Column(String)
    Slug = Column(String)
    Year_Served = Column(Integer)

class UsersSchema(BaseModel):
    id: int
    Name: str
    Slug: str
    Year_Served: int

class Config:
    populate_by_name = True

Base.metadata.create_all(engine)
