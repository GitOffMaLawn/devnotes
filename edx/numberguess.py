# Guess number program
l_h_c = ''
guess = 50
low_num = 0
high_num = 100

print("Please think of a number between 0 and 100!")

while l_h_c != 'c':
    l_h_c = input("Is your secret number " + str(guess) + " ?\n"
        "Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")
    if l_h_c == 'h':
        tmp = low_num + guess
        high_num = guess
        guess = tmp // 2
    elif l_h_c == 'l':
        tmp = high_num + guess
        low_num = guess
        guess = tmp // 2
    elif l_h_c == 'c':
        print("Game over. Your secret number was: {}".format(int(guess)))
    else:
        print("Sorry, I did not understand your input.")