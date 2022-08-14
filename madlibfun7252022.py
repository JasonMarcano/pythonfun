# -*- coding: utf-8 -*-
"""
Created on Sun Jul 24 23:43:10 2022

@author: Jason
"""

noun_1 = input("Enter a noun: ")
noun_2 = input("Enter a different noun: ")
noun_3 = input("Enter one last noun: ")

plural_noun_1 = input("Enter a PLURAL noun: ")
plural_noun_2 = input("Enter one more PLURAL noun: ")

num1 = input("Enter a number (no decimals): ")
num2 = input("Enter one more number (no decimals): ")

verb = input("Enter a verb that ends in \'ed\' or is past tense: ")

print("There once was an old " + noun_1 + " who had " + num1 + plural_noun_1 + ".")
print("The old " + noun_1 + " gave half of their " + plural_noun_1 + " to their" + noun_2 + ".")
print("Well, " + noun_2 + " really needed some " + plural_noun_2 + "," "so they " + verb)
print(" the " + plural_noun_1 + " and made " + num2 + " dollars to buy " + plural_noun_2 )
print(" so they could put them in their " + noun_3)