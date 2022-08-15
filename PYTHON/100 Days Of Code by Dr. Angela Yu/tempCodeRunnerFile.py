while add_card:
        another_card = input("Type 'y' to get another card, type 'n' to pass: ")
        if  another_card == "y":
            user_card = randint(1, card)
            user_card_list += [user_card]
            user_score += user_card
            print(f"Your cards: {user_card_list}, current score: {user_score}")
            if user_score > 21:
                print(f"Your final hand: {user_card_list}, final score: {user_score}")
                print("You went over. You lose 😭")
                add_card = False
        elif another_card == "n":
            print(f"Your final hand: {user_card_list}, final score: {user_score}")
            computer_list = []
            computer_list += [computer_card]
            computer_score += computer_card
            print(f"Your