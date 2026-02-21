from pydantic import BaseModel
from datetime import datetime

class Transaction(BaseModel):
    timestamp: datetime
    amount: float
    ceiling: float
    remanent: float