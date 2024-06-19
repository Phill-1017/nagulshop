from fastapi import APIRouter, HTTPException
from starlette.responses import JSONResponse
from repository.repository import saveBid, getBids
from basemodel.CreateBidRequest import CreateBidRequest

bidRouter = APIRouter()

@bidRouter.post("/bid")
def create_bid(bid: CreateBidRequest):
    try:
        success = saveBid(bid)
        if success is True:
            return JSONResponse(status_code=201, content={'message': 'Success'})
        else:
            return JSONResponse(status_code=406, content={'message': 'Bid too late or doesn\'t meet the requirements'})
    except Exception as e:
        print(e)
        return JSONResponse(content={"message": "Error"}, status_code=500)

@bidRouter.get("/bid/{offer_id}")
def get_all_bids(offer_id: int):
    try:
        bids = getBids(offer_id)
        return bids
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail="Error retrieving bids")
