print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
print("In the treasure you will find the purpose of life !!\n")
# https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

# Write your code below this line 👇
user_choice1 = input(
    'You are walking on the narrow round you came across a big opstacle.\nWhich way will you go ? "left or right" ?\n').lower()

if user_choice1 == "right":
    print("You just beat one of the opstacle of life and are one step ahead keep going !!\n")

    user_choice2 = input(
        'You just came accros a gaint wall with a hole at the bottom.\nWhat are you going to do ? "climb or crawl" ?\n').lower()

    if user_choice2 == "climb":
        print("You got did again, in life hard work pays of the marathon continue's, let's get it !!\n")

        user_choice3 = input(
            'Now you came accros an ocean what you are going to do ?\nAre you going to jump and swim, wait on a boat or grab the kayak at the shore and start peddaling ? "swim, boat or kayak"\n').lower()

        if user_choice3 == "kayak":
            print("You got it !!\nYou have open the treasure of life and the purpose of life is this.\nLife is a marathon not a sprint. Everything you want you have to go get it and that require Dedication, Hard Work, Plus Patient and Sacrifice")
        elif user_choice3 == "boat":
            print("You can keep on waiting the boat is not comming.\nNo one will come to help or save you.\nYou have to be able to help yourself !!")
        else:
            print("You just got ate by a bunch of sharks, because you don't have the right mindset relax life will happen when you have patients")
    else:
        print(
            "You just like the easy way out huh ? Your dead the wall collaps !! Game over ")
else:
    print("You just got burned and gave up on life! Game over")
