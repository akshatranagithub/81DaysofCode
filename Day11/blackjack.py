import os
import random

from art import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def hit():
    return int(random.choice(cards))


def calculate_score(cards_list):
    if 11 in cards_list and sum(cards_list) > 21:
        cards_list.remove(11)
        cards_list.append(1)
    return sum(cards_list)


def clear():
    os.system("cls")


def compare(first_list, second_list):
    first_sum = calculate_score(first_list)
    second_sum = calculate_score(second_list)

    if first_sum > 21 and second_sum > 21:
        print("Dealer wins")
    elif first_sum > 21:
        print("You Lose")
    elif second_sum > 21:
        print("Computer Lose")
    elif first_sum == second_sum:
        print("Tie")
    elif first_sum == 21 or first_sum > second_sum:
        print("You win")
    else:
        print("Computer wins")


choice = 'y'

while choice == 'y':
    choice = input("Do you want to play a game of Blackjack? Type 'y' or 'n':")
    if choice == 'y':
        clear()
        print(logo)

        user_cards = [hit(), hit()]
        calculate_score(user_cards)
        print(f"Your cards: {user_cards}")
        computer_cards = [hit()]
        print(f"Computer cards: {computer_cards}")
        user__game_choice = input("Type 'y' to get another card, type 'n' to pass: ")
        computer_cards.append(hit())
        if user__game_choice == 'y':
            user_cards.append(hit())
        if calculate_score(computer_cards) < 17:
            computer_cards.append(hit())

        print(f"Your cards: {user_cards}")
        print(f"Computer cards: {computer_cards}")
        compare(user_cards, computer_cards)
