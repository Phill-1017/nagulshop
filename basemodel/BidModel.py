import datetime
from pydantic import BaseModel
class BidModel(BaseModel):
    id: int
    offer_id: int
    bidder_id: int
    bid_amount: int
    timestamp: datetime.datetime
