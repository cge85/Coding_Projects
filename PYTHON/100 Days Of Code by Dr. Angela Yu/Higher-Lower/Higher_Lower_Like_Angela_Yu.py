import random
from art import logo, vs
from game_data import data
import os

def clear(): return os.system("cls")

def get_random():
    return random.choice(data)

def random_user(user):
    name = user["name"]
    description = user["description"]
    country = user["country"]
    return f"{name}, a {description}, from {country}."

def is_true(guess, a_follower, b_follower):
    if a_follower > b_follower:
        return guess == "a"
    else:
        return guess == "b"

score = 0
should_continue = True
print(logo)
user_b = get_random()

while should_continue:
    user_a = user_b
    user_b = get_random()
    while user_a == user_b:
        user_b = get_random()

    a_follower = user_a["follower_count"]
    b_follower = user_b["follower_count"]

    print(random_user(user_a))
    print(vs)
    print(random_user(user_b))

    guess = input("Who has more followers? Type 'A' or 'B':").lower()

    clear()
    print(logo)

    if is_true(guess, a_follower, b_follower):
        score += 1
        print(f"You're right! Current score: {score}.")
    else:
        should_continue = False
        print(f"Sorry, that's wrong. Final score: {score}.")
