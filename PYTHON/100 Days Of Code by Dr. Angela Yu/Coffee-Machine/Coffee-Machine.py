from data import MENU
from Logo import logo

print(logo)
power_on = True

es_water = MENU["espresso"]["ingredients"]['water']
es_coffee = MENU["espresso"]["ingredients"]['coffee']
es_cost = MENU["espresso"]["cost"]


la_water = MENU["latte"]["ingredients"]['water']
la_coffee = MENU["latte"]["ingredients"]['coffee']
la_milk = MENU["latte"]["ingredients"]['milk']
la_cost = MENU["latte"]["cost"]

ca_water = MENU["cappuccino"]["ingredients"]['water']
ca_coffee = MENU["cappuccino"]["ingredients"]['coffee']
ca_milk = MENU["cappuccino"]["ingredients"]['milk']
ca_cost = MENU["cappuccino"]["cost"]


user_insert_coins = 0
change = 0



while power_on:
    water = 300
    milk = 200
    coffee = 100
    money = 0
    print_report = f"Water: {water}ml\nMilk: {milk}ml\nCoffee: {coffee}g\nMoney: ${money}"

    user_choice = input("What would you like? (espresso/latte/cappuccino): ")
    

    if user_choice == "espresso":
        print("Please insert coins.")
        quaters = float(input("how many quaters?: "))
        user_insert_coins += quaters * 0.25
        dimes = float(input("how many dimes?: "))
        user_insert_coins += dimes * 0.10
        nickles = float(input("how many nickles?: "))
        user_insert_coins += nickles * 0.05
        pennies = float(input("how many pennies?: "))
        user_insert_coins += pennies * 0.01
        if user_insert_coins > es_cost:
            if es_water < water and es_coffee < coffee:
                water - es_water
                coffee - es_coffee
                money + es_cost
            change = float(round(user_insert_coins - es_cost, 2))
            print(f"Here is ${change} in change.")
            print("Here is your espresso ☕. Enjoy!")
        else:
            print("Sorry that's not enough money. Money refunded.")

    elif user_choice == "latte":
        print("Please insert coins.")
        quaters = float(input("how many quaters?: "))
        user_insert_coins += quaters * 0.25
        dimes = float(input("how many dimes?: "))
        user_insert_coins += dimes * 0.10
        nickles = float(input("how many nickles?: "))
        user_insert_coins += nickles * 0.05
        pennies = float(input("how many pennies?: "))
        user_insert_coins += pennies * 0.01
        if user_insert_coins > la_cost:
            if la_water < water and la_coffee < coffee and la_milk < milk:
                water -= la_water
                coffee -= la_coffee
                milk -= la_milk
                money += la_cost
            change = float(round(user_insert_coins - la_cost, 2))
            print(f"Here is ${change} in change.")
            print("Here is your latte ☕. Enjoy!")
        else:
            print("Sorry that's not enough money. Money refunded.")

    elif user_choice == "cappuccino":
        print("Please insert coins.")
        quaters = float(input("how many quaters?: "))
        user_insert_coins += quaters * 0.25
        dimes = float(input("how many dimes?: "))
        user_insert_coins += dimes * 0.10
        nickles = float(input("how many nickles?: "))
        user_insert_coins += nickles * 0.05
        pennies = float(input("how many pennies?: "))
        user_insert_coins += pennies * 0.01
        if user_insert_coins > ca_cost:
            if ca_water < water and ca_coffee < coffee and ca_milk < milk:
                water -= ca_water
                coffee -= ca_coffee
                milk -= ca_milk
                money += ca_cost
            change = float(round(user_insert_coins - ca_cost, 2))
            print(f"Here is ${change} in change.")  
            print("Here is your cappuccino ☕. Enjoy!")
        else:
            print("Sorry that's not enough money. Money refunded.")
    
    elif user_choice == "report":
        print(print_report)

    elif user_choice == "off":
        power_on = False

