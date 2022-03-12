def coffee_bot():
    print('Welcome to the cafe !')
    size = get_size()
    drink_type = get_drink_type()
    cup_type = type_of_cup()
    temp_coffee = temp_of_coffee()
    add_order = additional_order()
    print(f"Alright, that's a {temp_coffee} {size} {drink_type} in a {cup_type} !")
    name = input('Can I get your name please?')
    print(f'Thanks, {name}! Your drink will be ready shortly.')
    

def get_size():
    res = input('What size drink can I get for you? \n[a] Small \n[b] Medium \n[c] Large \n> ')
    if res == 'a':
        return 'Small'
    elif res == 'b':
        return 'Medium'
    elif res == 'c':
        return 'Large'
    else:
        print_message()
        return get_size()

def print_message():
    print("I'm sorry, I did not understand your selection. Please enter the corresponding letter for your response.")

def get_drink_type():
    res = input('What type of drink would you like? \n[a] Brewed coffee \n[b] Mocha \n[c] Latte \n> ')
    if res == 'a':
        return 'Brewed coffee'
    elif res == 'b':
        return 'Mocha'
    elif res == 'c':
        return order_latte()
    else:
        print_message()
        return get_drink_type()
    
def order_latte():
    res = input('And what kind of milk for your latte? \n [a] 2% milk \n [b] Non-fat milk \n [c] Soy milk \n> ')
    if res == 'a':
        return '2% milk'
    elif res == 'b':
        return 'non-fat milk'
    elif res == 'c':
        return 'soy latte'
    else:
        print_message()
        return order_latte()

def type_of_cup():
    res = input('What type of cup would yu like to use? \n [a] Plastic cup \n [b] Own reusable cup \n> ')
    if res == 'a':
        return 'Plastic cup'
    elif res == 'b':
        return 'Own reusable cup'
    else:
        print_message()
        return type_of_cup()

def temp_of_coffee():
    res = input('Would your like your coffee hot or cold? \n [a] Hot \n [b] Cold \n ')
    if res == 'a':
        return 'Hot'
    elif res == 'b':
        return 'Cold'
    else:
        print_message()
        return temp_of_coffee()

def additional_order():
    res = input('Would you like an additional order? \n [a] Yes \n [b] No \n> ')
    if res == 'a':
        size = get_size()
        drink_type = get_drink_type()
        cup_type = type_of_cup()
        temp_coffee = temp_of_coffee()


coffee_bot()
