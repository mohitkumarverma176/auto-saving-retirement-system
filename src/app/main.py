import math
from datetime import datetime
from typing import List, Dict, Any

# Data models
class Expense:
    def __init__(self, date: str, amount: int):
        self.date = datetime.strptime(date, "%Y-%m-%d %H:%M:%S")
        self.amount = amount

class Period:
    def __init__(self, start: str, end: str, value: int):
        self.start = datetime.strptime(start, "%Y-%m-%d %H:%M:%S")
        self.end = datetime.strptime(end, "%Y-%m-%d %H:%M:%S")
        self.value = value

# Utility functions

def round_up_to_100(amount: int) -> int:
    return math.ceil(amount / 100) * 100

def calculate_remanent(expense: Expense) -> int:
    return round_up_to_100(expense.amount) - expense.amount

# Apply q period rules (fixed amount override)
def apply_q_period(expense: Expense, q_periods: List[Period]) -> int:
    applicable = [p for p in q_periods if p.start <= expense.date <= p.end]
    if not applicable:
        return None
    # Use the one with the latest start date
    applicable.sort(key=lambda p: p.start, reverse=True)
    return applicable[0].value

# Apply p period rules (extra amount addition)
def apply_p_period(expense: Expense, p_periods: List[Period]) -> int:
    return sum(p.value for p in p_periods if p.start <= expense.date <= p.end)

# Group by k periods
def group_by_k_periods(expenses: List[Expense], remanents: List[int], k_periods: List[Period]) -> Dict[str, int]:
    grouped = {}
    for k in k_periods:
        total = sum(rem for exp, rem in zip(expenses, remanents) if k.start <= exp.date <= k.end)
        grouped[f"{k.start.strftime('%Y-%m-%d %H:%M:%S')} to {k.end.strftime('%Y-%m-%d %H:%M:%S')}"] = total
    return grouped

# Compound interest calculation
def compound_interest(P: float, r: float, t: int) -> float:
    return P * ((1 + r) ** t)

# Inflation adjustment
def inflation_adjust(A: float, inflation: float, t: int) -> float:
    return A / ((1 + inflation) ** t)

# Tax calculation (simplified slabs)
def calculate_tax(income: int) -> int:
    tax = 0
    if income > 1500000:
        tax += (income - 1500000) * 0.3
        income = 1500000
    if income > 1200000:
        tax += (income - 1200000) * 0.2
        income = 1200000
    if income > 1000000:
        tax += (income - 1000000) * 0.15
        income = 1000000
    if income > 700000:
        tax += (income - 700000) * 0.1
    return int(tax)

# NPS deduction and tax benefit
def nps_deduction(invested: int, annual_income: int) -> int:
    return min(invested, int(annual_income * 0.1), 200000)

def nps_tax_benefit(income: int, invested: int) -> int:
    deduction = nps_deduction(invested, income)
    return calculate_tax(income) - calculate_tax(income - deduction)

# Main processing function
def process_expenses(expenses: List[Expense], q_periods: List[Period], p_periods: List[Period], k_periods: List[Period], age: int, salary: int, inflation: float) -> Dict[str, Any]:
    remanents = []
    for exp in expenses:
        rem = calculate_remanent(exp)
        q_rem = apply_q_period(exp, q_periods)
        if q_rem is not None:
            rem = q_rem
        rem += apply_p_period(exp, p_periods)
        remanents.append(rem)
    grouped = group_by_k_periods(expenses, remanents, k_periods)
    years = max(60 - age, 5)
    results = {}
    for period, total in grouped.items():
        nps_return = compound_interest(total, 0.0711, years)
        nps_real = inflation_adjust(nps_return, inflation, years)
        nps_tax = nps_tax_benefit(salary * 12, total)
        index_return = compound_interest(total, 0.1449, years)
        index_real = inflation_adjust(index_return, inflation, years)
        results[period] = {
            "NPS_final": nps_return,
            "NPS_real": nps_real,
            "NPS_tax_benefit": nps_tax,
            "Index_final": index_return,
            "Index_real": index_real
        }
    return results

# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
