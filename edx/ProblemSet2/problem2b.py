

def calc_payoff(bal, month, mpguess, mpgavg=0.0):
    if month > 0:
        mpgavg = mpguess + mpgavg
        nmpg = (bal + (bal * annualInterestRate)) / month
        nbal = bal + (bal * annualInterestRate / 12) - nmpg
        return calc_payoff(nbal, month-1, nmpg)

    elif nbal < -2.0:
        return calc_payoff(bal, month = 12, mpguess, -1.0)

    elif nbal > 2.0:
        return calc_payoff(bal, month = 12, nmpg = 1.0)

    else:
        return mpgavg / 12

balance = 500
annualInterestRate = .2
mpguess = (balance + (balance * annualInterestRate)) / 12

print("Lowest Payment: ", round(calc_payoff(balance, 12, mpguess)))

# print("Test Case 1")
# balance = 3329
# annualInterestRate = 0.2
# print("Lowest Payment: ", round(calc_payoff(balance)))
# print("Lowest Payment: 310 -- correct")

# print("Test Case 2:")
# balance = 4773
# annualInterestRate = 0.2
# print("Lowest Payment: ", round(calc_payoff(balance)))
# print("Lowest Payment: 440 -- correct")

# print("Test Case 3:")
# balance = 3926
# annualInterestRate = 0.2
# print("Lowest Payment: ", round(calc_payoff(balance)))
# print("Lowest Payment: 360 -- correct")