import random
from art import logo, vs
from game_data import data
import os

def clear(): return os.system("cls")


print(logo)

def random_choice():
    random_choice_data = random.choice(data)
    name = random_choice_data['name']
    follower_count = random_choice_data['follower_count']
    description = random_choice_data['description']
    country = random_choice_data['country']
    return name, follower_count, description, country

compare_a = random_choice()
compare_b = random_choice()
follower_a = compare_a[1]
follower_b = compare_b[1]
print(follower_a)
print(follower_b)
print(f"Compare A:  {compare_a[0]}, a {compare_a[2]}, from {compare_a[3]}.")
print(f"Compare A:  {compare_b[0]}, a {compare_b[2]}, from {compare_b[3]}.")

input("Who has more followers? Type 'A' or 'B': ").upper()

score = 0
if follower_a > follower_b:


# # print(f"Compare A:  {name}, a {description}, from {country}.")

# print(vs)

# print(f"Against B:  {name}, a {description}, from {country}.")

# more_followers = input("Who has more followers? Type 'A' or 'B': ")




