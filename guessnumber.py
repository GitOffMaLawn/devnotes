#!/bin/env python3

# Guess the random number

import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    
    while guess != random_number:
        guess = int(input(f"Guess a number between 1 and {x}: "))
        if guess < random_number:
            print("You are too low")
        elif guess > random_number:
            print("Your are too high")
    
    return print(f"you are correct, the number was {guess}")

guess(10)