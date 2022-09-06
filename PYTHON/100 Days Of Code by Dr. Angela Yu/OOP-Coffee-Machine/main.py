from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffe_machine_on = True

menu = Menu()
coffe_maker = CoffeeMaker()
money_machine = MoneyMachine()

while coffe_machine_on:
    coffee_choices = menu.get_items()
    choices = input(f"What would you like? ({coffee_choices}) :")
    if choices == "off":
        coffe_machine_on = False
    elif choices == "report":
        coffe_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choices)
        if coffe_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffe_maker.make_coffee(drink)