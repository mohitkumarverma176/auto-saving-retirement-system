from src.app.model.transaction import Transaction
from src.app.util.math_utils import round_up_100


def build_transaction(expenses):
    transactions = []
    for expense in expenses:
        ceiling = round_up_100(expense.amount)
        remanent = ceiling - expense.amount
        transactions.append(Transaction(
            timestamp=expense.timestamp,
            amount=expense.amount,
            ceiling=ceiling,
            remanent=remanent
        ))
    return transactions