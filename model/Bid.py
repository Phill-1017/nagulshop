import datetime

from sqlalchemy import Column, Integer, String, Date, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Bid(Base):


    __tablename__ = 'bids'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    offer_id = Column(Integer, index=True)
    bidder_id = Column(Integer, index=True)
    bid_amount = Column(Integer, index=False)
    timestamp = Column(DateTime, index=False)

    def __init__(self, offer_id, bidder_id, bid_amount, timestamp):
        self.offer_id = offer_id
        self.bidder_id = bidder_id
        self.bid_amount = bid_amount
        self.timestamp = timestamp



