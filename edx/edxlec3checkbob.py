# DO NOT INCLUDE S = in submit
s = 'azcbobobeggbbobboobobbooobhakl'


numBobs = 0
letterB1 = 'n'
letterO = 'n'
letterB2 = 'n'
tempB2 = 'n'
count = 0
bob = 'n'
for char in s:
    print(char)
    if bob == 'bob':
        print("bob found")
        numBobs += 1
        letterB1 = 'n'
        letterB2 = 'n'
        letterO = 'n'
        bob = 'n'
        # print(input("bob var cleared.."))

        # print(input("start if in bob true if"))
        # if tempB2 == 'b' and char == 'o':
        #     #1.b
        #     letterB1 = tempB2
        #     letterO = 'o'
        #     tempB2 = 'n'
        #     print(input("ran w 1.b"))
        # elif char == 'b':
        #     #2
        #     letterB1 = 'b'
        #     print(input("ran w 2"))
        # elif char == 'o':
        #     #3
        #     letterO = 'o'
        #     print(input("ran w 3"))
        
        # print(f"{letterB1} {letterO} {letterB2} pause after bob if")

    print(input("start regular if"))
    if letterB1 == 'b' and char != 'o':
        letterB1 = 'n'
        letterO = 'n'
        letterB2 = 'n'
        tempB2 = 'n'
        print("ran 1")
    elif letterB1 == 'b' and letterO == 'o' and char != 'b':
        letterB1 = 'n'
        letterO = 'n'
        letterB2 = 'n'
        tempB2 = 'n'
        print("ran 2")
    elif letterB1 == 'b' and letterO == 'o' and char == 'b':
        letterB2 = 'b'
        tempB2 = 'b'
        bob = 'bob'
        print(input("ran 3"))
    elif tempB2 == 'b' and char == 'o':
        letterB1 = tempB2
        letterO = 'o'
        tempB2 = 'n'
        print(input("ran 4"))
    elif char == 'b':
        letterB1 = 'b'
        print(input("ran 5"))
    elif char == 'o':
        letterO = 'o'
        print(input("ran 6"))
    elif char == 'b' and tempB2 == 'b':
        letterB1 = 'b'
        print(input("ran 7"))
    elif letterB1 == 'b' and letterO == 'o' and letterB2 == 'b':
        bob = 'bob'
        print(input("ran 8"))
    else:
        letterB1 = 'n'
        letterB2 = 'n'
        letterO = 'n'
        print("ran else")
    
    print(input(f"{letterB1} {letterO} {letterB2} {tempB2} {numBobs} pause after reg if"))

print('Number of times bob occurs is: ' + str(numBobs))