import asyncio
from basemodel.AccountRequest import AccountRequest
from basemodel.CreateBidRequest import CreateBidRequest
from basemodel.LoginRequest import LoginRequest
from basemodel.CreateOfferRequest import CreateOfferRequest
from basemodel.Message import MessageModel
from router.AccountRouter import loginAccount, registerAccount
from router.BidRouter import create_bid, get_all_bids
from router.ShoeOfferRouter import postOffer, getAllOffers
from router.MessageRouter import post_message, read_messages

def run_async(task):
    try:
        loop = asyncio.get_running_loop()
    except RuntimeError:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
    return loop.run_until_complete(task)

def register(args):
    account_request = AccountRequest(username=args.username, password=args.password, role=args.role)
    run_async(registerAccount(account_request))
    print("Registration process complete.")

def login(args, post_login_callback):
    login_request = LoginRequest(username=args.username, password=args.password)
    result = run_async(loginAccount(login_request))
    if result:
        print(f"Login successful for {args.username}.")
        user_role = result.role
        post_login_callback(args, user_role)
    else:
        print("Login failed or user not found.")

def create_offer(args):
    offer_request = CreateOfferRequest(name=args.name, price=args.price, description=args.description)
    run_async(postOffer(offer_request))
    print("Offer creation process completed.")

def offers(args):
    offers = run_async(getAllOffers())
    if offers:
        for offer in offers:
            print(f"Offer ID: {offer.id}, Name: {offer.name}, Price: {offer.price}, Description: {offer.description}")
    else:
        print("No offers found.")

def message(args):
    message = MessageModel(sender=args.sender, receiver=args.receiver, message=args.message_text)
    result = run_async(post_message(message))
    print("Message posted successfully.")

def show_messages(args):
    try:
        messages = run_async(read_messages(args.receiver, next(get_db())))
        if messages:
            for msg in messages.messages:
                print(f"From: {msg.sender}, Message: {msg.text}")
        else:
            print("No messages found.")
    except Exception as e:
        print(f"Error: {str(e)}")

def create_bid_cli(args):
    bid_request = CreateBidRequest(offer_id=args.offer_id, bid_amount=args.bid_amount, bidder_id=args.bidder_id)
    result = run_async(create_bid(bid_request))
    print(result)

def get_bids(args):
    bids = run_async(get_all_bids(args.offer_id))
    if bids:
        for bid in bids:
            print(f"Bid ID: {bid.id}, Bidder ID: {bid.bidder_id}, Amount: {bid.bid_amount}")
    else:
        print("No bids found.")
