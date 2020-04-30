balance = 33
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

'''Ub = balance - Minimum_Payment
print("Unpaid Balance = ", Ub)
M_interest = (annualInterestRate/12.0) * Ub
print("Interest = ", M_interest)
Newbalance = Ub + (M_interest)
print("Monthly balance", Newbalance)'''

total_paid = 0
i = 0
while i < 12:
    print("------- Month " + str(i) + " -------")
    print("Month's balance", balance)
    Minimum_Payment = balance * monthlyPaymentRate
    rMinimum_Payment = round(Minimum_Payment, 2)
    print("Minimum Payment = ", rMinimum_Payment)
    total_paid = total_paid + rMinimum_Payment
    round(total_paid)
    Ub = balance - rMinimum_Payment
    rUb = round(Ub, 2)
    print("Unpaid Balance = ", rUb)
    M_interest = (annualInterestRate / 12.0) * rUb
    rM_interest = round(M_interest, 2)
    print("Interest = ", rM_interest)
    newbalance = rUb + rM_interest
    balance = round(newbalance, 2)
    i += 1

print("# Remaining balance = ", balance)
print("# Total paid = ", round(total_paid,2))