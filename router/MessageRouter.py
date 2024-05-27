from fastapi import APIRouter, Depends, HTTPException
from starlette.responses import JSONResponse
from sqlalchemy.orm import Session
from basemodel.MessageResponse import MessagesResponse, MessageDetail
from repository import repository
from model.Message import Message
from basemodel.Message import MessageModel
from repository.repository import get_db

messageRouter = APIRouter()

@messageRouter.post("", response_model=MessageModel)
async def post_message(message: MessageModel):
    try:
        msg = Message(sender=message.sender, receiver=message.receiver, message=message.message)
        repository.postMessage(msg)
        return JSONResponse(content={"message": "Success"}, status_code=200)
    except Exception as e:
        print(e)
        return JSONResponse(content={"message": "Error"}, status_code=500)

@messageRouter.get("/messages/{receiver}", response_model=MessagesResponse)
async def read_messages(receiver: str, db: Session = Depends(get_db)):
    messages = db.query(Message).filter(Message.receiver == receiver).all()
    if not messages:
        raise HTTPException(status_code=404, detail="No messages found for the receiver.")
    response = MessagesResponse(messages=[MessageDetail(sender=msg.sender, text=msg.message) for msg in messages])
    return response
