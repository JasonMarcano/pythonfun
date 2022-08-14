# -*- coding: utf-8 -*-
"""
Created on Fri Aug 12 19:13:41 2022

@author: Jason
"""

#rock paper scissors
# r > s, s > p, p > r

import random
print("Let's play rock, paper, scissors")
def rpsGame():
    user = input("Type 'r' for Rock, 'p' for paper, or 's' for scissors: " )
    comp = random.choice (['r', 'p', 's'])
    if user == comp:
       print('Tie! You chose:' ,user,  '& I chose:',  comp)
    if winRPS(user, comp):
        print('You win! You chose:' ,user,  '& I chose:',  comp)
    if winRPS(comp, user):
        print('You lost! You chose:' ,user, '& I chose:', comp)
    replay()
   
def winRPS(player, computer):
    if (player == 'r' and computer == 's') or (player == 'p' and computer == 'r') \
    or (player == 's' and computer == 'p'):
        return True
        
    
def replay():
    ans = input('Would you like to play again? Type y/n: ')
    if ans.lower() == 'n':
        print('Goodbye!')
    elif ans.lower() == 'y':
        rpsGame()
    else:
        print('Invalid Input')
        replay()
    
    
        
        
    
print(rpsGame())