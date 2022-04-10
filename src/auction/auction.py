from dataclasses import dataclass, field

from bid import Bid

@dataclass
class Auction:
    description :str
    bids: list[Bid] = field(default_factory=list[Bid])
