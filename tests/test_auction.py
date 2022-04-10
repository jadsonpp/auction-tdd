from unittest import TestCase
import unittest
import sys

sys.path.append("..")

from src.auction.auction import Auction
from src.auction.bid import Bid
from src.auction.user import User

class TestAuction(TestCase):
    def test_auction(self):
        bids = [
            Bid(User("Josh"), 55.5),
            Bid(User("Caitlyn"), 50.0),
            Bid(User("Lost"), 60.0)
        ]
        my_auction = Auction("Phone", bids)
        self.assertEqual(len(my_auction.bids), 3) # three bids
        self.assertEqual(my_auction.description, "Phone")

if __name__ == "__name__":
    unittest.main()