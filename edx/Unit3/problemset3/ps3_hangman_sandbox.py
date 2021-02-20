#!/bin/env python3

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    count = 0
    word_len = len(secretWord)
    if len(secretWord) == 0 or len(lettersGuessed) == 0:
          return False
    for i in secretWord:
        if i in lettersGuessed:
            count += 1
    return count == word_len


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    word_guessed = ''
    for i in secretWord:
        if i in lettersGuessed:
          word_guessed = word_guessed + i + ' '
        else:
          word_guessed = word_guessed + '_ '
            
    return word_guessed


def getAvailableLetters(lettersGuessed = ''):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    complete_alphabet = 'abcdefghijklmnopqrstuvwxyz'
    avail_letters = list(complete_alphabet)
    for i in lettersGuessed:
        if i in lettersGuessed:
            avail_letters.remove(i)

    return ''.join(avail_letters)

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
    guess_count = 8
    available_letters = getAvailableLetters()
    secretWord_L = list(secretWord)
    used_letters = ''
    myUsedDict = {}
    print("Welcome to the game, Hangman!")
    print("I am thinking of a word that is", len(secretWord),"letters long.")
    print("-------------")
    
    while guess_count != 0:
        print("You have", guess_count,"guesses left.")
        print("Available letters: ", available_letters)
        letter_guess = input("Please guess a letter: ").lower()
        available_letters = getAvailableLetters(letter_guess)
        available_letters_L = list(available_letters)
        used_letters = used_letters + letter_guess
        used_letters_L = list(used_letters)
        myUsedDict
        
        if letter_guess in myUsedDict:
            # if repeat letter print
            print("Oops! You've already guessed that letter: ", getGuessedWord(secretWord, myUsedDict))
            print("-------------")
    
        elif letter_guess in secretWord_L:
            # if good guess print
            print("Good guess: ", getGuessedWord(secretWord, myUsedDict))
            print("-------------")
            if isWordGuessed(secretWord, myUsedDict) == True:
                return print("Congratulations, you won!")
                
        elif letter_guess not in secretWord_L:
            # if letter not in word print
            guess_count -= 1
            print("Oops! That letter is not in my word: ", getGuessedWord(secretWord, myUsedDicta))
            print("-------------")
            
    return print("Sorry, you ran out of guesses. The word was else.")

secretWord = 'apple'
# secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
