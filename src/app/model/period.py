from datetime import datetime
from pydantic import BaseModel

class QPeriod(BaseModel):
    start: datetime
    end: datetime
    fixed: float


class PPeriod(BaseModel):
    start: datetime
    end: datetime
    extra: float

class KPeriod(BaseModel):
    start: datetime
    end: datetime