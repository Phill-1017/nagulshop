from pydantic import BaseModel
from typing import List

class MessageDetail(BaseModel):
    sender: str
    text: str

class MessagesResponse(BaseModel):
    messages: List[MessageDetail]
