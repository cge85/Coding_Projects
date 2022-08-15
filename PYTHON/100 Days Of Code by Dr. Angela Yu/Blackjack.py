from Blackjack_art import logo
from random import randint
import os


def clear(): return os.system('cls')


print(logo)


def play_blackjack():
    input("Do You want to play a game of Blackjack? Type 'y' or 'n': ")
    clear()
    print(logo)
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    user_add_card = True
    computer_add_card = True

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

    while user_add_card:
        another_card = input(
            "Type 'y' to get another card, type 'n' to pass: ")
        if another_card == "y":
            user_card = randint(1, card)
            user_card_list += [user_card]
            user_score += user_card
            if user_score > 21:
                print(
                    f"Your final hand: {user_card_list}, final score: {user_score}")
                print(
                    f"Computer's final hand: {computer_card_list}, final score: {computer_score}")
                print("You went over. You lose 😭\n")
                user_add_card = False
            else:
                print(
                    f"Your cards: {user_card_list}, current score: {user_score}")
                print(f"Computer's first card: {computer_card}")

        elif another_card == "n":
            while computer_add_card:
                if computer_score < 21:
                    computer_card = randint(1, card)
                    computer_card_list += [computer_card]
                    computer_score += computer_card
                    if computer_score <= 21 and computer_score > user_score:
                        print(
                            f"Your final hand: {user_card_list}, final score: {user_score}")
                        print(
                            f"Computer's final hand: {computer_card_list}, final score: {computer_score}")
                        print("Computer Win Better Luck Next Time.\n")
                        computer_add_card = False
                elif computer_score == 21 and user_score == 21:
                    print(
                        f"Your final hand: {user_card_list}, final score: {user_score}")
                    print(
                        f"Computer's final hand: {computer_card_list}, final score: {computer_score}")
                    print("It Is A Draw.\n")
                    computer_add_card = False
                else:
                    print(
                        f"Your final hand: {user_card_list}, final score: {user_score}")
                    print(
                        f"Computer's final hand: {computer_card_list}, final score: {computer_score}")
                    print("Congratulations, You Win.\n")
                    computer_add_card = False
            play_blackjack()
    play_blackjack()
play_blackjack()
