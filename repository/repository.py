import datetime

from sqlalchemy import create_engine, Table, Column, String, Integer, MetaData, Float, ForeignKey, Date, DateTime
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from basemodel import CreateBidRequest
from basemodel.AccountRequest import AccountRequest
from basemodel.LoginRequest import LoginRequest
from basemodel.LoginResponse import LoginResponse
from basemodel.CreateOfferRequest import CreateOfferRequest
from model.Bid import Bid

from model.Message import Message
from model.Account import Account
from model.ShoeOffer import ShoeOffer

import os


Base = declarative_base()
DATABASE_URL = os.getenv('DB_URL', "postgresql+psycopg2://lfgrljdrln:Postgres10@naguldatabase.postgres.database.azure.com:5432/nagulshopapp-database")
engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(autocommit=False, bind=engine)
db = SessionLocal()

metadata = MetaData()

accounts = Table('accounts', metadata,
                 Column('id', Integer, primary_key=True, autoincrement=True),
                 Column('username', String, unique=True),
                 Column('password', String),
                 Column('role', String)
                 )

messages = Table('messages', metadata,
                 Column('id', Integer, primary_key=True, autoincrement=True),
                 Column('sender', String),
                 Column('receiver', String),
                 Column('message', String))

shoeoffers = Table('shoeoffers', metadata,
                   Column('id', Integer, primary_key=True, autoincrement=True),
                   Column('name', String),
                   Column('price', Float),
                   Column('description', String),
                   Column('seller_id', Integer)  #
                   )
bid = Table('bids', metadata,
            Column('id', Integer, primary_key=True, autoincrement=True),
            Column('offer_id', Integer, ForeignKey('shoeoffers.id')),
            Column('bidder_id', Integer, ForeignKey('accounts.id')),
            Column('bid_amount', Integer),
            Column('timestamp', DateTime))
metadata.create_all(engine)


def postMessage(message: Message):
    db.add(message)
    db.commit()
    db.flush()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


async def register(account: AccountRequest):
    try:
        db.add(Account(username=account.username, password=account.password, role=account.role))
        db.commit()
        db.flush()
    except SQLAlchemyError as e:
        db.rollback()
        raise SQLAlchemyError


async def login(loginRequest: LoginRequest):
    acc = db.query(Account).filter(Account.username == loginRequest.username).first()
    if acc and acc.password == loginRequest.password:
        return LoginResponse(id=acc.id, username=acc.username, role=acc.role)  # Include id in the response
    else:
        return None


async def createOffer(request: CreateOfferRequest):
    try:
        db.add(ShoeOffer(name=request.name, price=request.price, description=request.description,
                         #seller_id=request.seller_id
                         ))
        db.commit()
    except SQLAlchemyError as e:
        db.rollback()
        raise SQLAlchemyError


async def getAll():
    try:
        offers = db.query(ShoeOffer).all()
        return offers
    except SQLAlchemyError as e:
        db.rollback()
        raise SQLAlchemyError


async def fetchOffer(id: int):
    try:
        offer = db.query(ShoeOffer).filter(ShoeOffer.id == id).first()
        return offer
    except SQLAlchemyError as e:
        db.rollback()
        raise SQLAlchemyError


async def saveBid(request: CreateBidRequest):
    try:
        print(request)
        first_bid = db.query(Bid).filter(Bid.offer_id == request.offer_id).first()
        print("first_bid")
        last_bid = db.query(Bid).filter(Bid.offer_id == request.offer_id).order_by(Bid.id.desc()).first()
        print("second bid")
        curr_date = datetime.datetime.now()
        if first_bid is None:
            db.add(Bid(offer_id=request.offer_id, bidder_id=request.bidder_id, bid_amount=request.bid_amount,
                       timestamp=curr_date))
            db.commit()
            return True
        elif abs((curr_date - first_bid.timestamp).seconds < 120) and (last_bid.bid_amount + 5) <= request.bid_amount:
            db.add(Bid(offer_id=request.offer_id, bidder_id=request.bidder_id, bid_amount=request.bid_amount,
                       timestamp=curr_date))
            db.commit()
            return True
        else:
            print(first_bid.bid_amount)
            print(last_bid.bid_amount)
            return None
    except SQLAlchemyError as e:
        print("ERRRRRRRRRRRRRRRRRRRRRR")
        print(e)
        db.rollback()
        raise SQLAlchemyError


async def getBids(offer_id: int):
    try:
        bids = db.query(Bid).filter(Bid.offer_id == offer_id).all()
        return bids
    except SQLAlchemyError as e:
        db.rollback()
        raise SQLAlchemyError

