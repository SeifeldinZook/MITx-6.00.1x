balance = 3926
annualInterestRate = 0.2

def does_minimum_work(balance, annualInterestRate, Minimum_Payment):

    for i in range(0, 12):
        rMinimum_Payment = round(Minimum_Payment, 2)
        Ub = balance - rMinimum_Payment
        rUb = round(Ub, 2)
        M_interest = (annualInterestRate / 12.0) * rUb
        rM_interest = round(M_interest, 2)
        newbalance = rUb + rM_interest
        balance = round(newbalance, 2)

    if Ub > 0:
        return False
    else:
        return True


for j in range(1, balance, 1):
    if does_minimum_work(balance, annualInterestRate, j) == False:
        continue
    else:
        print("Lowest Payment:", j)
        break
