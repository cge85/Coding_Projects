from operator import index
from Blackjack_art import logo
from random import randint
import os

clear = lambda: os.system('cls')





def play_blackjack():
    print(logo)
    print(input("Do You want to play a game of Blackjack? Type 'y' or 'n': "))
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]




    add_card = True
    
    for card in cards:
        user_card1 = randint(1, card)
        user_card2 = randint(1, card)
        user_card_list = [user_card1, user_card2]
        user_score = user_card1 + user_card2
        computer_card = randint(1, card)
        computer_card_list = [computer_card]
        computer_score = computer_card
    print(f"Your cards: {user_card_list}, current score: {user_score}")
    print(f"Computer's first card: {computer_card}")
    
    while add_card:
        another_card = input("Type 'y' to get another card, type 'n' to pass: ")
        if  another_card == "y" and user_score < 21:
                user_card = randint(1, card)
                user_card_list += [user_card]
                user_score += user_card
                print(f"Your cards: {user_card_list}, current score: {user_score}")
        else:
            print(f"Your final hand: {user_card_list}, final score: {user_score}")
            print(f"Computer's final hand: {computer_card_list}, final score: {computer_score}")
            print("You went over. You lose 😭")
            add_card = False

        if another_card == "n":
            computer_card_list += computer_card
            computer_score += computer_card_list[computer_card]
            if computer_score < 21 and computer_score > user_score:
                print(f"Your final hand: {user_card_list}, final score: {user_score}")
                print(f"Computer's final hand: {computer_card_list}, final score: {computer_score}")
                print("Computer Win")
        # else:
        #     print(f"Your final hand: {user_card_list}, final score: {user_score}")
        #     print(f"Computer's final hand: {computer_card_list}, final score: {computer_score}")
        #     print("You went over. You lose 😭")
        #     add_card = False
play_blackjack()