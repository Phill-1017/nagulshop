from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base();

class Account(Base):

    __tablename__ = 'accounts'

    id = Column(Integer, index=True, primary_key=True, autoincrement=True)
    username = Column(String, index=True, primary_key=True)
    password = Column(String, index=True)
    role = Column(String, index=True)
