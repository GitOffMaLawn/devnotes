def isIn(char, aStr):
    if char == aStr[len(aStr) // 2]:
        return True
    elif aStr == '':
        return False
    elif char < aStr[len(aStr) // 2]:
        ne = len(aStr) // 2
        if ne == 0:
            return False
        return isIn(char, aStr[:ne])
    elif char > aStr[len(aStr) // 2]:
        ns = len(aStr) // 2
        if ns == 0:
            return False
        return isIn(char, aStr[ns:])

print(isIn('k', 'abcdefghijkl'))
print(isIn('k', ''))