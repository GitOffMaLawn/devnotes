"""
Problem set1 project edX

Calculate the balance at the end of a year.

These variables and values are provided:

annualInterestRate
monthlyPaymentRate
balance



"""


def calculate_balance(bal, month):
    if month > 0:
        pay = monthlyPaymentRate * bal
        nbal = float(bal) - pay
        return calculate_balance((nbal + (annualInterestRate / 12) * nbal), month-1)
    else:
        return round(bal, 2)

balance = 100
annualInterestRate = .20
monthlyPaymentRate = .02
print("Remaining balance:", calculate_balance(balance, 12))

balance = 42
annualInterestRate = 0.2
monthlyPaymentRate = 0.04
print("Remaining balance: {}".format(calculate_balance(balance, 12)))
print("Remaining balance: 31.38")

balance = 484
annualInterestRate = 0.2
monthlyPaymentRate = 0.04
print("Remaining balance: {}".format(calculate_balance(balance, 12)))
print("Remaining balance: 361.61")

balance = 445
annualInterestRate = 0.22
monthlyPaymentRate = 0.04
print("Remaining balance: {}".format(calculate_balance(balance, 12)))
print("Remaining balance: 339.07")

balance = 226
annualInterestRate = 0.15
monthlyPaymentRate = 0.04
print("Remaining balance: {}".format(calculate_balance(balance, 12)))
print("Remaining balance: 160.73")
