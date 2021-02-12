


balance = 100.0
monthlyPaymentRate = .02
annualInterest = .13

per_ofbalance = monthlyPaymentRate / 1 * balance
int_onbalance = balance + (annualInterest / 12.0) * balance

new_balance = int_onbalance - per_ofbalance


print("New balance after Interest: balance + (interest / 12 months) * balance --- {}".format(int_onbalance))
print("Percentage of balance: percent / 1 * balance --- {}".format(per_ofbalance))
print("New balance after payment: int_onbalance - per_ofbalance --- {}".format(round(new_balance, 2)))
print("New balance after payment no round: int_onbalance - per_ofbalance --- {}".format(new_balance))
