from dataclasses import dataclass, field

@dataclass
class Auction:
    description :str
    bids: list = field(default_factory=list) 
