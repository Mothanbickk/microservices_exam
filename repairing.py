from dataclasses import dataclass
from typing import Optional


@dataclass
class Repairing:
    description: str
    city: str
    price: int
    loss_estimate: int
    amount: int
    created: str = ""
    status: str = "new"
    id: Optional[int] = None
