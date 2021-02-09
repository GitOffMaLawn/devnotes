s = 'jfhdxyzhhsasntehoerrcbbinabcbcdbsgtabcuvhhdhfjfiklm'

char1 = ''
char2 = ''
ochar = 0
ochar1 = 0
ochar2 = 0
omatch = 0
obestmatch = 9999
check = ''
newMatch = 0
bestmatch = ''

for char in s:
    ochar = ord(char)
    cochar = ochar1 + 1
    cochar1 = ochar2 + 1

    if ochar == cochar and ochar1 == cochar1:
        newMatch += 1
        omatch = ochar2 + ochar1 + ochar
        if omatch < obestmatch:
            bestmatch = char2 + char1 + char
            obestmatch = omatch


    char2 = char1
    char1 = char
    ochar2 = ochar1
    ochar1 = ochar

print(f"Longest substring in alphabetical order is:", bestmatch)
