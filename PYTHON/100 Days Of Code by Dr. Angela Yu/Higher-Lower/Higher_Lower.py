import random
from art import logo, vs
from game_data import data
import os

def clear(): return os.system("cls")

def game():
    def random_choice_data():
        return random.choice(data)

    def random_info(user_data):
        name  = user_data["name"]
        description = user_data["description"]
        country = user_data["country"]
        return f"{name}, a {description}, from {country}."

    print(logo)
    score = 0
    should_continue = True
    user_b = random_choice_data()

    while should_continue:    
        user_a = user_b
        user_b = random_choice_data()
        while user_a == user_b:
            user_b = random_choice_data()

        followers_a = user_a["follower_count"]
        followers_b = user_b["follower_count"]

        print(f"Compare A: {random_info(user_a)}")
        print(vs)
        print(f"Against B: {random_info(user_b)}")

        guess = input("Who has more followers? Type 'A' or 'B': ").lower()
        
        clear()
        print(logo)

        if guess == "a":
            if followers_a > followers_b:
                score += 1
                print(f"You're right! Current score: {score}")
            else:
                should_continue = False
                print(f"Sorry, that's wrong. Final score: {score}")
        else:
            if followers_b > followers_a:
                score += 1
                print(f"You're right! Current score: {score}")
            else:
                should_continue = False
                print(f"Sorry, that's wrong. Final score: {score}")
game()