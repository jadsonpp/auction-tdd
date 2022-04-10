from unittest import TestCase
import unittest
import sys
sys.path.append("..")

from src.auction.bid import Bid
from src.auction.user import User

class TestBid(TestCase):
    def test_bid(self):
        john = User("John Lennon")
        johns_bids = Bid(john, 80.50)
        self.assertEqual(johns_bids.value, 80.50) 

if __name__ == "__name__":
    unittest.main()