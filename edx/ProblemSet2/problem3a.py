"""
Problem set2 project edX
Calculate a fixed payment using bisection
to pay off balance in 12 months.

These variables and values are provided:
balance
annualInterestRate
"""

# Calculations that may be needed
# Monthly interest rate = (Annual interest rate) / 12.0
# Monthly payment lower bound = Balance / 12
# Monthly payment upper bound = (Balance x (1 + Monthly interest rate)12) / 12.0
# +/- .2

def calc_payoff(bal, month = 12, guessrun = 0.0):
    nbal = bal
    while month > 0:
        nbal = round(bal + (bal * (annualInterestRate / 12)), 2) - round(guessrun, 2)
        return calc_payoff(nbal, month-1, guessrun)
    return nbal

def calc_accurate(bal, mpgl, mpgh):
    guess = round((mpgl + mpgh) / 2, 2)
    bal = calc_payoff(balance, 12, guess)
    tttry = 5
    while tttry != 0:
        if bal < -.01:
            mpgh = guess
            guess = (mpgl + mpgh) / 2
            bal = calc_payoff(balance, 12, guess)
            tttry -= 1
        elif bal > .01:
            mpgl = guess
            guess = (mpgl + mpgh) / 2
            bal = calc_payoff(balance, 12, guess)
            tttry -= 1
    tttry = 5
    while tttry != 0:
        if bal < -.01:
            guess -= .01
            bal = calc_payoff(balance, 12, guess)
            tttry -= 1
        elif bal > .01:
            guess += .01
            bal = calc_payoff(balance, 12, guess)
            tttry -= 1
    return round(guess, 2)

balance = 320000
annualInterestRate = 0.2
mpglow = balance / 12
mpghigh = (balance + (balance * annualInterestRate)) / 12
print("Lowest Payment: ", calc_accurate(balance, mpglow, mpghigh))
print("Lowest Payment: 29157.09 -- correct")

balance = 999999
annualInterestRate = 0.18
mpglow = balance / 12
mpghigh = (balance + (balance * annualInterestRate)) / 12
print("Lowest Payment: ", calc_accurate(balance, mpglow, mpghigh))
print("Lowest Payment: 90325.03 -- correct")

balance = 320862
annualInterestRate = 0.2
mpglow = balance / 12
mpghigh = (balance + (balance * annualInterestRate)) / 12
print("Lowest Payment: ", calc_accurate(balance, mpglow, mpghigh))
print("Lowest Payment: 29235.63 -- correct")

balance = 493102
annualInterestRate = 0.22
mpglow = balance / 12
mpghigh = (balance + (balance * annualInterestRate)) / 12
print("Lowest Payment: ", calc_accurate(balance, mpglow, mpghigh))
print("Lowest Payment: 45320.7 -- correct")

balance = 429510
annualInterestRate = 0.18
mpglow = balance / 12
mpghigh = (balance + (balance * annualInterestRate)) / 12
print("Lowest Payment: ", calc_accurate(balance, mpglow, mpghigh))
print("Lowest Payment: 38795.54 -- correct")

balance = 228066
annualInterestRate = 0.22
mpglow = balance / 12
mpghigh = (balance + (balance * annualInterestRate)) / 12
print("Lowest Payment: ", calc_accurate(balance, mpglow, mpghigh))
print("Lowest Payment: 20961.4 -- correct")
