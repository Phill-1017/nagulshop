from fastapi import APIRouter, HTTPException
from starlette.responses import JSONResponse
from basemodel.MessageResponse import MessagesResponse, MessageDetail
from repository import repository
from model.Message import Message
from basemodel.Message import MessageModel

messageRouter = APIRouter()

@messageRouter.post("", response_model=MessageModel)
def post_message(message: MessageModel):
    try:
        msg = Message(sender=message.sender, receiver=message.receiver, message=message.message)
        repository.postMessage(msg)
        return JSONResponse(content={"message": "Success"}, status_code=200)
    except Exception as e:
        print(e)
        return JSONResponse(content={"message": "Error"}, status_code=500)

@messageRouter.get("/messages/{receiver}", response_model=MessagesResponse)
def read_messages(receiver: str):
    messages = repository.fetchMessages(receiver)
    if not messages:
        raise HTTPException(status_code=404, detail="No messages found for the receiver.")
    response = MessagesResponse(messages=[MessageDetail(sender=msg.sender, text=msg.message) for msg in messages])
    return response
