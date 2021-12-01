def compound_interest_amount(p, r, t, n):
    return p * (1 + r / n) ** (n * t)

def __main__():
    print(compound_interest_amount(1500000, 0.043, 6, 4))
    print(compound_interest_amount(1500000, 0.043, 6, 1/2))

__main__()
