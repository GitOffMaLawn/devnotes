"""
Problem set2 project edX

Calculate a fixed payment to pay off balance
in 12 months.

These variables and values are provided:

annualInterestRate
balance

Monthly interest rate = (Annual interest rate) / 12.0
Monthly unpaid balance = (Previous balance) - (Minimum fixed monthly payment)
Updated balance each month = (Monthly unpaid balance) + (Monthly interest rate x Monthly unpaid balance)

	      Test Case 1:
	      balance = 3329
	      annualInterestRate = 0.2

	      Result Your Code Should Generate:
	      -------------------
	      Lowest Payment: 310

          Test Case 2:
	      balance = 4773
	      annualInterestRate = 0.2
	      
	      Result Your Code Should Generate:
	      -------------------
	      Lowest Payment: 440

          Test Case 3:
	      balance = 3926
	      annualInterestRate = 0.2

	      Result Your Code Should Generate:
	      -------------------
	      Lowest Payment: 360
"""


def calculate_payoff(bal, month):
    if month > 0:
        pay = monthlyPaymentRate * bal
        nbal = float(bal) - pay
        return calculate_balance((nbal + (annualInterestRate / 12) * nbal), month-1)
    else:
        return round(bal, 2)

balance = 100
annualInterestRate = .20
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
