import webbrowser
from fastapi import FastAPI, HTTPException, Depends, status
from pydantic import BaseModel
from typing import List, Optional

from starlette.responses import FileResponse
from starlette.staticfiles import StaticFiles

from router.MessageRouter import messageRouter
from router.AccountRouter import accountRouter
from router.ShoeOfferRouter import offerRouter
#from router.ShoppingCartRouter import cartRouter
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session
import uvicorn

import os

#from router.ShoppingCartRouter import cartRouter

app = FastAPI()

# Mount the static directory
app.mount("/static", StaticFiles(directory="static"), name="static")

# Include routers
app.include_router(messageRouter, prefix="/message")
app.include_router(accountRouter, prefix='/account')
app.include_router(offerRouter, prefix='/shoe-offer')

# Serve the index.html file at the root URL
@app.get("/")
def read_root():
    return FileResponse('static/html/index.html')

@app.get("/register")
def register_user():
    return FileResponse('static/html/register.html')

@app.get("/home_admin")
def home_admin():
    return FileResponse('static/html/home_admin.html')

@app.get("/home")
def home_user():
    return FileResponse('static/html/home_user.html')

@app.get("/shop")
def shop_offer_page():
    return FileResponse('static/html/shop_all.html')

@app.get("/messages")
def create_offer_page():
    return FileResponse('static/html/messages_page.html')

@app.get("/send_message")
def create_offer_page():
    return FileResponse('static/html/create_message.html')

@app.get("/your_messages")
def create_offer_page():
    return FileResponse('static/html/view_user_messages.html')

@app.get("/create_offer")
def create_offer_page():
    return FileResponse('static/html/create_offer.html')


# Open the default web browser after server starts
@app.on_event("startup")
async def startup_event():
    webbrowser.open("http://127.0.0.1:8000")

# Running the server
if __name__ == "__main__":
    print(os.getenv('DB_URL'))
    uvicorn.run(app, host="0.0.0.0", port=8000)
