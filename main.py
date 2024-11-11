from card import Card

import random

suits = ("Spades", "Hearts", "Clubs", "Diamonds")
ranks = ("Two", "Three","Four","Five","Six","Seven","Eight","Nine","Ten", "Jack", "Queen", "King", "Ace")

print("Testing the Card Class")

card1 = Card(suits[2],ranks[4])
#Test the get functions
if card1.get_suit() == suits[2]:
    print("Passed suit test")
if card1.get_rank() == ranks[4]:
    print("Passed rank test")
if card1.get_value() == 6:
    print("Passed value test")

print(card1)#This should print the card from the __str__ method

card2 = Card(suits[0],ranks[12])
#Test the get functions
if card1.get_suit() == suits[0]:
    print("Passed suit test")
if card1.get_rank() == ranks[12]:
    print("Passed rank test")
if card1.get_value() == 11:
    print("Passed value test")

print(card2)#This should print the card from the __str__ method

card3 = Card(suits[3],ranks[11])
#Test the get functions
if card1.get_suit() == suits[3]:
    print("Passed suit test")
if card1.get_rank() == ranks[11]:
    print("Passed rank test")
if card1.get_value() == 10:
    print("Passed value test")

print(card3)#This should print the card from the __str__ method
