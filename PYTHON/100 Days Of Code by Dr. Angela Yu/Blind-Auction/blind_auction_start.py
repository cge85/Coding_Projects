import os
from blind_auction_start_logo import logo

clear = lambda: os.system('cls')

print(logo)

auction_dict = {}
more_bidders = True

while more_bidders:
    name = input("What is your name?: ")
    bid = int(input("What's your bid?: $"))
    auction_dict[name] = bid
    other_bidders = input("Are there any other bidders: Type 'yes' or 'no'.")
    if other_bidders == "no":
        more_bidders = False
    else:
        clear()

h_bid = 0
w_name = ""
for name in auction_dict:
    bids = auction_dict[name]
    if h_bid < bids:
        h_bid = bids
        w_name = name
print(f"The winner is {w_name} with a bid of ${h_bid}")
