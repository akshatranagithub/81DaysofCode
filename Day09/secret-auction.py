import os

from art import logo

print(logo)
print("Welcome to the secret auction program")


def clear():
    os.system("cls")


def get_highest_bidder(bidder_record):
    name = ""
    max_bid = -1.0
    for bidder, bid in bidder_record.items():
        if max_bid < bid:
            max_bid = bid
            name = bidder

    return name, bid


bidder_record = {}
choice = 'yes'
while choice == 'yes':
    name = input("What is your name: ").lower()
    bid = float(input("What is your bid: ₹"))
    bidder_record[name] = bid
    choice = input("Are there any other bidders? Type 'yes' or 'no': ").lower()
    if choice == "yes":
        clear()

name, bid = get_highest_bidder(bidder_record)

clear()
print(f"The winner is {name} with a bid of ₹{bid}")
