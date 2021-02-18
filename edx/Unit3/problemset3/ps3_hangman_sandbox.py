
def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    count = 0
    if len(secretWord) == 0 or len(lettersGuessed) == 0:
          return False
    for i in secretWord:
        if i in lettersGuessed:
            count += 1
    return count == 0


print(isWordGuessed('apple', ['a', 'e', 'i', 'k', 'p', 'r', 's']), "Correct is False")

print(isWordGuessed('durian', ['h', 'a', 'c', 'd', 'i', 'm', 'n', 'r', 't', 'u']), "Correct is True")

print(isWordGuessed('grapefruit', []), "Correct is False")

print(isWordGuessed('broccoli', ['z', 'x', 'q', 'b', 'r', 'o', 'c', 'c', 'o', 'l', 'i']), "Correct is True")

# Return 'False' or 'True'