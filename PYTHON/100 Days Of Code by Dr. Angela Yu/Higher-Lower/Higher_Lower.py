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

<<<<<<< HEAD
def get_random_choice():
    """Get data from game_data file"""
    return random.choice(data)

def format_data(game_data):
    """format data into printable format: name, description and country"""
    name = game_data['name']
    description = game_data['description']
    country = game_data['country']
    return f"{name}, a {description}, from {country}"

def check_answer(guess, follower_a, follower_b):
    """Check followers agains user's guess
    and return True if they got it right.
    Or False if they got it wrong."""  
    if follower_a > follower_b:
        return guess == "a"
    else:
        return guess == "b"

def game():
    print(logo)
    score = 0
    game_should_continue = True
    data_b = get_random_choice()

    while game_should_continue:
        data_a = data_b
        data_b = get_random_choice()
        
        while data_a == data_b:
            data_b = get_random_choice()
    
        print(f"Compare A: {format_data(data_a)}.")
        print(vs)
        print(f"Compare B: {format_data(data_b)}.")

        guess = input("Who has more followers? Type 'A' or 'B': ").lower()
        data_a_count = data_a["follower_count"]
        data_b_count = data_b["follower_count"]
        is_correct = check_answer(guess, data_a_count, data_b_count)

        clear()
        print(logo)
        if is_correct:
            score += 1
            print(f"You're right! Current score: {score}.")
        else:
            game_should_continue = False
            print(f"Sorry, that's wrong. Final score: {score}")

=======
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
>>>>>>> 55436935fe9ee98ea00039db2831495dc870002b
game()