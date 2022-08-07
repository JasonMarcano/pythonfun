# -*- coding: utf-8 -*-
"""
Created on Fri Aug  5 23:04:44 2022

@author: Jason
"""

import random
import sys



name = input("What is your name? ")


def guessing_game():
    n = random.randint(1, 50)
    guesses_made = 0
    print("Let's play a game", name)
    
    user_guess = int(input("Guess a number 1-50: "))
    
    while user_guess != n:
        print()
        if user_guess > n:
            print("That's too high!")
            guesses_made +=1
            user_guess = int(input("Guess lower: "))
        elif user_guess < n:
            print("That's too low!")
            user_guess = int(input("Guess Higher: "))
            guesses_made += 1
        
    
    if user_guess == n:
        print("Congratulations", name, "You guessed correctly in", guesses_made, "guesses.")
        another_round()
        
        
def another_round():
    choice = input("Would you like to play again? Enter y or n: ")
    if choice.lower() == "n":
        print("Goodbye, thanks for playing", name + "!")
    elif choice.lower() == "y":
       guessing_game()
    else:
        print("Invlaid input. Goodbye!")
      
    
    

guessing_game()


   
    
    

    