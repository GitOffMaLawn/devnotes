#!/usr/bin/env python3

"""
Problem set2 project edX

Calculate a fixed payment to pay off balance
in 12 months.

These variables and values are provided:

balance
annualInterestRate

Calculations that may be needed
Monthly interest rate = (Annual interest rate) / 12.0
Monthly unpaid balance = (Previous balance) - (Minimum fixed monthly payment)
Updated balance each month = (Monthly unpaid balance) + (Monthly interest rate x Monthly unpaid balance)


best so far 11/15
"""


def calc_payoff(bal, month = 12, guessrun = 0.0):
    if month > 0:
        mpguess = round((bal + (bal * annualInterestRate)) / month, -1)
        guessrun = mpguess + guessrun
        nbal = bal + (bal * annualInterestRate / 12) - mpguess
        return calc_payoff(nbal, month-1, guessrun)
    
    else:
        return round(guessrun / 12, -1)
        


balance = 500.0
annualInterestRate = .2
print("Lowest Payment: ", calc_payoff(balance))

print("Test Case 1")
balance = 3329
annualInterestRate = 0.2
print("Lowest Payment: ", calc_payoff(balance))
print("Lowest Payment: 310 -- correct")

print("Test Case 2:")
balance = 4773
annualInterestRate = 0.2
print("Lowest Payment: ", calc_payoff(balance))
print("Lowest Payment: 440 -- correct")

print("Test Case 3:")
balance = 3926
annualInterestRate = 0.2
print("Lowest Payment: ", calc_payoff(balance))
print("Lowest Payment: 360 -- correct")
