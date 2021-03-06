#!/bin/env python3

import random

complete_alphabet = 'abcdefghijklmnopqrstuvwxyz'
avail_letters_L = list(complete_alphabet)

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


def getAvailableLetters(letterGuessed = ''):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    if letterGuessed in avail_letters_L:
        avail_letters_L.remove(letterGuessed)
    return ''.join(avail_letters_L)

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
    secretWord_L = list(secretWord)
    used_letters_L = []
    print("Welcome to the game, Hangman!")
    print("I am thinking of a word that is", len(secretWord),"letters long.")
    print("-------------")
    
    while guess_count != 0:
        print("You have", guess_count,"guesses left.")
        print("Available letters:", getAvailableLetters(used_letters_L))
        letter_guess = input("Please guess a letter: ").lower()
        getAvailableLetters(letter_guess)
        
        if letter_guess in used_letters_L:
            # if repeat letter print
            print("Oops! You've already guessed that letter:", getGuessedWord(secretWord, used_letters_L))
            print("-------------")
            continue

        used_letters_L.append(letter_guess)
        
        if letter_guess in secretWord_L:
            # if good guess print
            print("Good guess:", getGuessedWord(secretWord, used_letters_L))
            print("-------------")
            if isWordGuessed(secretWord, used_letters_L) == True:
                return print("Congratulations, you won!")
                
        elif letter_guess not in secretWord_L:
            # if letter not in word print
            guess_count -= 1
            print("Oops! That letter is not in my word:", getGuessedWord(secretWord, used_letters_L))
            print("-------------")
            
    return print("Sorry, you ran out of guesses. The word was {}.".format(secretWord))

# secretWord = 'apple'
secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
