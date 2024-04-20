import os
from art import logo


print(logo)
bidders = "yes"

bids = {}


def find_highest_bidder(bid_record):
    highest_bid = 0
    for key in bid_record:
        current_bid = bid_record[key]
        if current_bid > highest_bid:
            highest_bid = current_bid
            winner = key

    print(f"The winner is {winner} with a bid of ${highest_bid}")


while bidders == "yes":
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: "))
    bids[name] = bid
    bidders = input("Are there any other bidders? Type 'yes or'no'.\n").lower()
    if bidders == "yes":
        os.system("cls")

find_highest_bidder(bids)
