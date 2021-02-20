# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    count = 0
    word_len = len(secretWord)
    if len(secretWord) == 0 or len(lettersGuessed) == 0:
          return False
    for i in secretWord:
        if i in lettersGuessed:
            count += 1
    return count == word_len


print(isWordGuessed('apple', ['a', 'e', 'i', 'k', 'p', 'r', 's']), "Correct is False")

print(isWordGuessed('durian', ['h', 'a', 'c', 'd', 'i', 'm', 'n', 'r', 't', 'u']), "Correct is True")

print(isWordGuessed('grapefruit', []), "Correct is False")

print(isWordGuessed('broccoli', ['z', 'x', 'q', 'b', 'r', 'o', 'c', 'c', 'o', 'l', 'i']), "Correct is True")



def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    word_guessed = ''
    for i in secretWord:
        if i in lettersGuessed:
          word_guessed = word_guessed + i + ' '
        else:
          word_guessed = word_guessed + '_ '
            
    return word_guessed

print(getGuessedWord('apple', ['a', 'e', 'i', 'k', 'p', 'r', 's']), "Correct is ' a p p _ e '")

print(getGuessedWord('durian', ['h', 'a', 'c', 'd', 'i', 'm', 'n', 'r', 't', 'u']), "Correct is ' d u r a i n '")

print(getGuessedWord('grapefruit', []), "Correct is ' _ _ _ _ _ _ _ _ _ '")

print(getGuessedWord('broccoli', ['z', 'x', 'q', 'r', 'o', 'c', 'c', 'o', 'l', 'i']), "Correct is ' _ r o c c o l i '")



def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    complete_alphabet = 'abcdefghijklmnopqrstuvwxyz'
    avail_letters = list(complete_alphabet)
    for i in lettersGuessed:
        if i in lettersGuessed:
            avail_letters.remove(i)

    return ''.join(avail_letters)

print(getAvailableLetters(['a', 'e', 'i', 'k', 'p', 'r', 's']), "Correct is 'bcdfghjlmnoqtuvwxyz'")


def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...






# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

# secretWord = chooseWord(wordlist).lower()
# hangman(secretWord)
