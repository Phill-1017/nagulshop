from typing import List
from pydantic import BaseModel
from basemodel.BidModel import BidModel
class GetBidsResponse(BaseModel):
    bids: List[BidModel]