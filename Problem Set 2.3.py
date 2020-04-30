balance = 999999
annualInterestRate = 0.2
epsilon = 0.01
monthlyinterestrate = annualInterestRate / 12.0
lowerbound = balance / 12
upperbound = (balance * (1 + monthlyinterestrate)**12) / 12.0
d = (upperbound - lowerbound) / 2


def does_minimum_work(balance, annualInterestRate, Minimum_Payment):

    for i in range(0, 12):
        rMinimum_Payment = round(Minimum_Payment, 2)
        Ub = balance - rMinimum_Payment
        rUb = round(Ub, 2)
        M_interest = (annualInterestRate / 12.0) * rUb
        rM_interest = round(M_interest, 2)
        newbalance = rUb + rM_interest
        balance = round(newbalance, 2)

    if rUb > 0:
        return False
    else:
        return True


while (upperbound - lowerbound) > epsilon:
    d = (upperbound - lowerbound) / 2
    mid = lowerbound + d
    # lower ----- lower + d -------upper
    if does_minimum_work(balance, annualInterestRate, mid):
        upperbound = mid
    else:
        lowerbound = mid


if does_minimum_work(balance, annualInterestRate, lowerbound):
    print( "Lowest Payment:", round(lowerbound,2))
elif does_minimum_work(balance, annualInterestRate, (lowerbound+d)):
    print("Lowest Payment:", round(lowerbound+d, 2))
else:
    print("Lowest Payment:", round(upperbound, 2))
