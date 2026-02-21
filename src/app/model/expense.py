from pydantic import BaseModel
from datetime import datetime


class Expense(BaseModel):
    timestamp: datetime
    amount: float