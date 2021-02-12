"""
Problem set1 project edX

Calculate the balance at the end of a year.

These variables and values are provided:

annualInterestRate
monthlyPaymentRate
balance

balance = 484; annualInterestRate = 0.2; monthlyPaymentRate = 0.04
Remaining balance: 361.61
balance = 445; annualInterestRate = 0.22; monthlyPaymentRate = 0.04
Remaining balance: 339.07
balance = 226; annualInterestRate = 0.15; monthlyPaymentRate = 0.04
Remaining balance: 160.73

"""

month = 11
def calculate_balance(bal, month):
    for m in range(1, month):
        return calculate_balance((monthlyPaymentRate * bal) - (bal + (annualInterestRate / 12) * bal), month-1)
    return round(bal, 2)

balance = 100
annualInterestRate = .20
monthlyPaymentRate = .02

print("Remaining balance: {}".format(calculate_balance(balance, 12)))

balance = 42
annualInterestRate = 0.2
monthlyPaymentRate = 0.04
print("Remaining balance: {}".format(calculate_balance(balance, 12)))
print("Remaining balance: 31.38")