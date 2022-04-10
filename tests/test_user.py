from unittest import TestCase
import unittest
import sys
sys.path.append("..")

from src.auction.user import User

class TestUser(TestCase):
    def test_user(self):
        john = User("John Lennon")
        self.assertEqual(john.name, "John Lennon") 

if __name__ == "__name__":
    unittest.main()