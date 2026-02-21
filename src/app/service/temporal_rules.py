from functools import total_ordering

from Scripts.pdf2txt import extract_text

from src.app.util.date_utils import in_range

def apply_q_p_rules(transactions, q_rules, p_rules):
    for transaction in transactions:
        applicable_q = [
            q for q in q_rules
            if in_range(transaction.timestamp, q.start_date, q.end_date)
        ]
        if applicable_q:
            chosen = max(applicable_q, key=lambda x: x.start)
            transaction.remanent = chosen.fixed

        extra = sum(
            p.extra for p in p_rules
            if in_range(transaction.timestamp, p.start_date, p.end_date)
        )
        transaction.remanent += extra
    return transactions

def evaluate_k_periods(transactions, k_periods):
    results = []
    for k in k_periods:
        total = sum(
            t.remanent for t in transactions
            if in_range(t.timestamp, k.start_date, k.end_date)
        )
        results.append({
            "start": k.start_date,
            "end": k.end_date,
            "amount": total
        })
    return transactions