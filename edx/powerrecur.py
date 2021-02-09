
def recurPower(base, exp):
    if exp == 0:
        return 1.0000
    elif exp == 1:
        return base
    else:
        return base * recurPower(base, exp-1)


print(recurPower(6, 6))
print(6**6)
print(recurPower(6.74, 8))
print(6.74**8)
print(recurPower(-6.74, 8))
print(-6.74**8)
print(recurPower(-2.85, 2))
print(-2.85**2)
print(recurPower(-4.18, 4))
print(-4.18**4)