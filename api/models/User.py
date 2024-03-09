from sqlalchemy import Column, Integer, String, Text, ForeignKey
from pydantic import BaseModel
from db import engine 
from models.Base import Base

class Users(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True,)
    email = Column(String)
    Password = Column(String)

class UsersSchema(BaseModel):
    id: int
    email: str
    Password: str

class Config:
    populate_by_name = True

Base.metadata.create_all(engine)
