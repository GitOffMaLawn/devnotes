# DO NOT INCLUDE S = in submit
s = 'azcbobobeggbbobboobobbooobhbob'


numBobs = 0
char1 = 'n'
char2 = 'n'
bob = 'n'
for char in s:
    print(input(f"char {char}, char1 {char1}, char2 {char2}"))
    bob = str(char + char1 + char2)
    if bob == 'bob':
        print("found one more bob!")
        numBobs += 1
    char2 = char1
    char1 = char

print('Number of times bob occurs is: ' + str(numBobs))