import cmath
import random
from art import logo, vs
from game_data import data
import os

def clear(): return os.system("cls")


# print(logo)

def random_choice():
    random_choice_data = random.choice(data)
    name = random_choice_data['name']
    follower_count = random_choice_data['follower_count']
    description = random_choice_data['description']
    country = random_choice_data['country']
    return name, follower_count, description, country


compare_a = random_choice()
compare_b = random_choice()
compare_c = random_choice()

if compare_a == compare_b:
    compare_b = compare_c

def compare_followers():
    compare_followers = input("Who has more followers? Type 'A' or 'B': ").upper()
    score = 0
    followers_a = compare_a[1]
    followers_b = compare_b[1]
    if compare_followers == "A":
        if followers_a > followers_b:
            score += 1
            return print(f"You're right! Current score: {score}.")
        else:
            return print(f"Sorry, that's wrong. Final score: {score}")
    else:
        if followers_b > followers_a:
            score += 1
            return print(f"You're right! Current score: {score}.")
        else:
            return print(f"Sorry, that's wrong. Final score: {score}")



print(logo)

print(f"Compare A:  {compare_a[0]}, a {compare_a[2]}, from {compare_a[3]}.")

print(vs)

print(f"Against B:  {compare_b[0]}, a {compare_b[2]}, from {compare_b[3]}.")
compare_followers()



# compare_a = random_choice()
# compare_b = random_choice()
# compare_c = random_choice()

# if compare_a == compare_b:
#     compare_b = compare_c

# print(f"Compare A:  {compare_a[0]}, a {compare_a[2]}, from {compare_a[3]}.")

# print(vs)

# print(f"Against B:  {compare_b[0]}, a {compare_b[2]}, from {compare_b[3]}.")

# followers_a = compare_a[1]
# followers_b = compare_b[1]
# print(followers_a)
# # print(followers_b)
# score = 0

# is_true = True
# while is_true:
#     compare_a = random_choice()
#     compare_b = random_choice()
#     compare_c = random_choice()

#     # if compare_a == compare_b:
#     #     compare_b = compare_c
    
#     followers_a = compare_a[1]
#     followers_b = compare_b[1]
#     print(followers_a)
#     print(followers_b)

    
#     print(f"Compare A:  {compare_a[0]}, a {compare_a[2]}, from {compare_a[3]}.")

#     print(vs)

#     print(f"Against B:  {compare_b[0]}, a {compare_b[2]}, from {compare_b[3]}.")

#     compare_followers = input("Who has more followers? Type 'A' or 'B': ").upper()
#     if compare_followers == "A":
#         if followers_a > followers_b:
#             score += 1
#             compare_a = compare_b
#             print(f"You're right! Current score: {score}.")
#         else:
#             print(f"Sorry, that's wrong. Final score: {score}")
#             is_true = False
#     else:
#         if followers_b > followers_a:
#             score += 1
#             compare_a = compare_b
#             print(f"You're right! Current score: {score}.")
#         else:
#             print(f"Sorry, that's wrong. Final score: {score}")
#             is_true = False





