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


"""



def calc_payoff(bal, month = 12, guessrun = 0.0):
    if month > 0:
        mpguess = (bal + (bal * annualInterestRate)) / month
        guessrun = mpguess + guessrun
        nbal = bal + (bal * annualInterestRate / 12) - mpguess
        return calc_payoff(nbal, month-1, guessrun)
		
    else:
        return guessrun / 12




print("my test")
balance = 500
annualInterestRate = .2
print("Lowest Payment: ", round(calc_payoff(balance)))

print("Test Case 1")
balance = 3329
annualInterestRate = 0.2
print("Lowest Payment: ", round(calc_payoff(balance)))
print("Lowest Payment: 310 -- correct")

print("Test Case 2:")
balance = 4773
annualInterestRate = 0.2
print("Lowest Payment: ", round(calc_payoff(balance)))
print("Lowest Payment: 440 -- correct")

print("Test Case 3:")
balance = 3926
annualInterestRate = 0.2
print("Lowest Payment: ", round(calc_payoff(balance)))
print("Lowest Payment: 360 -- correct")
