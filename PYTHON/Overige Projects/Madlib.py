# string concatenation (aka how to put strings together)
# Suppose we want to create a string that says "subscribe to ____"
# youtuber = "Cliffton Emers" # some string variable

# # a few ways to do this
# print("subscribe to " + youtuber)
# print("subscribe to {}".format(youtuber))
# print(f"subscribe to {youtuber}")

adj = input("Adjetive: ")
verb1 = input("Verb: ")
verb2 = input("verb2: ")
famous_person = input("Famous person: ")

madlib = f"Computer programming is so {adj}! \
It makes me so excited all the time because \
I love to {verb1}. Stay hydrated and {verb2} \
like you are {famous_person}!"

print(madlib)