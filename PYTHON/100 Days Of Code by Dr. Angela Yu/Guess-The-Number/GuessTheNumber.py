import random
from GuessTheNumberLogo import logo
import os

def clear(): return os.system('cls')

def play_guessing_game():
    print(logo)

    print("Welcome to the Number Guessing Game!")
    print("I'm thinking about a number between 1 and 100.")
    random_guessed_number = random.choice(range(1,101))
    print(f"Pssst, the correct answer is {random_guessed_number}")

    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if difficulty == "easy":
        attempts = 10
        print(f"You have {attempts} attempts remaining to guess the number.")
    else:
        attempts = 5
        print(f"You have {attempts} attempts remaining to guess the number.")

    while attempts != 0:
        user_guess_number = int(input("Make a guess: "))
        if user_guess_number < random_guessed_number:
            attempts -= 1
            print("Too low.")
            print("Guess again")
            print(f"You have {attempts} attempts remaining to guess the number.")
        elif user_guess_number > random_guessed_number:
            attempts -= 1
            print("Too High.")
            print("Guess again")
            print(f"You have {attempts} attempts remaining to guess the number.")
        else:
            return print(f"You got it! The answer was {random_guessed_number} ")
    print("You've run out of guesses, you lose.")

play_guessing_game()

