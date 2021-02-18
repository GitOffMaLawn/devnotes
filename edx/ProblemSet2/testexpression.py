
bal = 500.0
# monthlyPaymentRate = .02
annualInterest = .20

# per_ofbalance = monthlyPaymentRate / 1 * balance
# int_onbalance = balance + (annualInterest / 12.0) * balance

# new_balance = int_onbalance - per_ofbalance

nbal = bal + (bal * annualInterest)
mpguess = nbal / 12

## f strings don't work in EDX!

print(f"New balance after Interest: balance + (interest / 12 months) * balance --- {onemonthint}")

# print(f"New balance after Interest: balance + (interest / 12 months) * balance --- {onemonthint}")
# print(f"Percentage of balance: percent / 1 * balance --- {per_ofbalance}")
# print(f"New balance after payment: int_onbalance - per_ofbalance --- {round(new_balance, 2)}")
# print(f"New balance after payment no round: int_onbalance - per_ofbalance --- {new_balance}")
