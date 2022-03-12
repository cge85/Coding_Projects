start_points = 100
round1 = 3
while round1 >= 0:
    user_input = input()
    if user_input == 'hit':
        start_points += 10
    elif user_input == 'miss':
        start_points -= 20
    round1 -= 1
print(start_points)