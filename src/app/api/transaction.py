from fastapi import APIRouter
from typing import List
from src.app.model.expense import Expense
from src.app.service.transaction_builder import build_transaction



router = APIRouter()


@router.post("/build")
def build_transaction(expenses: List[Expense]):
    return build_transaction(expenses)