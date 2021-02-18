
def iterPower(base, exp):
    prod = base
    if exp == 0:
        return 1.0000
    # elif base < 0:
    #     for i in range(0, exp-1):
    #         base *= -prod
    #     return base
    else:
        for i in range(0, exp-1):
            base *= prod
        return base


print(iterPower(6, 6))
print(6**6)
print(iterPower(6.74, 0))
print(6.74**0)
print(iterPower(6.74, 8))
print(6.74**8)
print(iterPower(-6.74, 8))
print(-6.74**8)
print(iterPower(-2.85, 2))
print(-2.85**2)
print(iterPower(-4.18, 4))
print(-4.18**4)