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
    zbal = bal
    while month > 0:
        aftpay = bal - guessrun
        zbal = (aftpay * (annualInterestRate / 12)) + aftpay
        return calc_payoff(zbal, month-1, guessrun)
    return zbal

def calc_accurate(guess, mpgl, mpgh):
    nbal = calc_payoff(balance, 12, guess)
    epsilon = 2
    while nbal < -epsilon or nbal > epsilon:
        if nbal < -epsilon:
            mpgh = guess
            guess = (mpgl + mpgh) / 2
            nbal = calc_payoff(balance, 12, guess)
        elif nbal > epsilon:
            mpgl = guess
            guess = (mpgl + mpgh) / 2
            nbal = calc_payoff(balance, 12, guess)
    return round(guess, 2)

balance = 320000
annualInterestRate = 0.2
mpglow = balance / 12
mpghigh = (balance + (balance * annualInterestRate)) / 12
fguess = (mpglow + mpghigh) / 2
print("Lowest Payment:", calc_accurate(fguess, mpglow, mpghigh))
print("Lowest Payment: 29157.09 -- correct")

balance = 346226
annualInterestRate = 0.2
mpglow = balance / 12
mpghigh = (balance + (balance * annualInterestRate)) / 12
fguess = (mpglow + mpghigh) / 2
print("Lowest Payment:", calc_accurate(fguess, mpglow, mpghigh))
print("Lowest Payment: 31546.7 -- correct")

balance = 71831
annualInterestRate = 0.18
mpglow = balance / 12
mpghigh = (balance + (balance * annualInterestRate)) / 12
fguess = (mpglow + mpghigh) / 2
print("Lowest Payment:", calc_accurate(fguess, mpglow, mpghigh))
print("Lowest Payment: 6488.14 -- correct")

