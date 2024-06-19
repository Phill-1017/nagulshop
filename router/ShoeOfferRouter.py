from fastapi import APIRouter, HTTPException
from starlette import status
from starlette.responses import JSONResponse
from repository.repository import createOffer, getAll, fetchOffer
from basemodel.CreateOfferRequest import CreateOfferRequest

offerRouter = APIRouter()

@offerRouter.post("/create")
def postOffer(request: CreateOfferRequest):
    try:
        createOffer(request)
        return JSONResponse(content={"meesage": "Success"}, status_code=200)
    except:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Internal server error")

@offerRouter.get("/all")
def getAllOffers():
    try:
        offers = getAll()
        return offers
    except:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Internal server error")

@offerRouter.get("")
def getOffer(id: int):
    try:
        offer = fetchOffer(id)
        if offer is None:
            return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="ID Not found")
        return offer
    except:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Internal server error")