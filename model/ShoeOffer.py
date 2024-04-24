from sqlalchemy import Integer, String, Float, Column
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class ShoeOffer(Base):

    __tablename__ = 'shoeoffers'

    id = Column(Integer, index=True, primary_key=True, autoincrement=True)
    name = Column(String, index=True)
    price = Column(Float, index=True)
    description = Column(String, index=True)
    #seller_id = Column(Integer, index=True)