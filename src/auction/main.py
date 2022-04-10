
from bid import Bid
from evaluator import Evaluator
from user import User
from auction import Auction

# Users
john = User("John Lennon")
slash = User("Slash")

# Bids
johns_bids = Bid(john, 80.50)
slash_bids = Bid(slash, 70.00)

# Auctions
phone_auction = Auction("Phone")
phone_auction.bids.append(johns_bids)
phone_auction.bids.append(slash_bids)

# Evaluator
auction_evaluator = Evaluator()
auction_evaluator.processing_auction(phone_auction)
print(f"Highest Bid: R$ {auction_evaluator.max_value}  Lowest Bid: R$ {auction_evaluator.min_value}.")
