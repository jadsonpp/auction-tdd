
from unittest import TestCase
import unittest
import sys
sys.path.append("..")

from src.auction.auction import Auction
from src.auction.bid import Bid
from src.auction.evaluator import Evaluator

from src.auction.user import User


class TestEvaluator(TestCase):

    def test_evaluator(self):
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

        min_expected_value, max_expected_value = 70.00, 80.50
        self.assertEqual(min_expected_value, auction_evaluator.min_value)
        self.assertEqual(max_expected_value, auction_evaluator.max_value)


if __name__ == "__name__":
    unittest.main()