from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Message(Base):
    __tablename__ = 'messages'
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    sender = Column(String, index=True)
    receiver = Column(String, index=True)
    message = Column(String, index=True)

    def __init__(self, sender, receiver, message):
        self.sender = sender
        self.receiver = receiver
        self.message = message



