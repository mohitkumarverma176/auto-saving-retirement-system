def compound(p, rate, years):
    return p * (1 + rate) ** years

def inflation_adjustment(amount, inflation_rate, years):
    return amount / (1 + inflation_rate) ** years