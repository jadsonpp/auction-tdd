
from dataclasses import dataclass
from .auction import Auction
import sys

@dataclass
class Evaluator:

    max_value: int = sys.float_info.min
    min_value: int = sys.float_info.max

    def processing_auction(self, auction: Auction):
        for bid in auction.bids:
           
            if bid.value > self.max_value:
                self.max_value = bid.value
            elif bid.value < self.min_value:
                self.min_value = bid.value
            
            print(self.max_value)

           
    


