from dataclasses import dataclass
from user import User

@dataclass
class Bid:
    user: User
    value: float

