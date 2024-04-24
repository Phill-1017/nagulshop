
class BidModel:
    def __init__(self, id, offer_id, bidder_id, bid_amount, timestamp):
        self.id = id
        self.offer_id = offer_id
        self.bidder_id = bidder_id
        self.bid_amount = bid_amount
        self.timestamp = timestamp