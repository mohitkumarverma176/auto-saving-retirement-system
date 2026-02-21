from fastapi import APIRouter
from typing import List
from src.app.model.transaction import Transaction
from src.app.model.period import QPeriod, PPeriod, KPeriod
from src.app.service.temporal_rules import apply_q_p_rules, evaluate_k_periods
from src.app.service.investement import compound, inflation_adjustment

router = APIRouter()

@router.post("/returns:index")
def index_returns(
    age: int,
    inflation: float,
    transactions: List[Transaction],
    q: List[QPeriod],
    p: List[PPeriod],
    k: List[KPeriod]
):
    years = max(60 - age, 5)
    tx = apply_q_p_rules(transactions, q, p)
    results = evaluate_k_periods(tx, k)

    for r in results:
        final = compound(r["amount"], 0.1449, years)
        r["return"] = inflation_adjustment(final, inflation, years)

    return results