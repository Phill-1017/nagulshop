import webbrowser
from fastapi import FastAPI
from starlette.staticfiles import StaticFiles
from router.MessageRouter import messageRouter
from router.AccountRouter import accountRouter
from router.ShoeOfferRouter import offerRouter
from router.BidRouter import bidRouter
from fastapi.responses import FileResponse
import uvicorn
import os
from frontend import cli

app = FastAPI()


app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(messageRouter, prefix="/message")
app.include_router(accountRouter, prefix='/account')
app.include_router(offerRouter, prefix='/shoe-offer')
app.include_router(bidRouter, prefix='/bid')


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
def messages_page():
    return FileResponse('static/html/messages_page.html')

@app.get("/send_message")
def send_message_page():
    return FileResponse('static/html/create_message.html')

@app.get("/view_messages")
def your_message_page():
    return FileResponse('static/html/view_user_messages.html')

@app.get("/create_offer")
def create_offer_page():
    return FileResponse('static/html/create_offer.html')

@app.on_event("startup")
async def startup_event():
    webbrowser.open("http://127.0.0.1:8000")

if __name__ == "__main__":
    print(os.getenv('DB_URL'))
    uvicorn.run(app, host="127.0.0.1", port=8000)
