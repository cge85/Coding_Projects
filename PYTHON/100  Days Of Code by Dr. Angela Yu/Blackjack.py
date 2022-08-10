from operator import index
from Blackjack_art import logo
from random import randint
import os

clear = lambda: os.system('cls')


play = input("Do You want to play a game of Blackjack? Type 'y' or 'n': ")

print(logo)

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def user_draw():
    for card in cards:
        user_card1 = randint(1, card)
        user_card2 = randint(1, card)
        user_cards = [user_card1, user_card2]
        score = user_card1 + user_card2
    print(f"Your cards: {user_cards}, current score: {score}")
user_draw()

def computer_draw():
    for card in cards:
        computer_card1 = randint(1, card)
    print(f"Computer's first card: {computer_card1}")
computer_draw()

if input("Type 'y' to get another card, type 'n' to pass: ") == "y":
    user_card3 = 