from art import logo
from art import vs
import random
from game_data import data
import os

game_score = 0

while 1:
    os.system('cls')
    print(logo)

    if game_score > 0:
        print(f"You are right! Current score: {game_score}")

    first_person = random.choice(data)
    print(f"Compare A: {first_person['name']}, a {first_person['description']}, from {first_person['country']}")

    print(vs)

    second_person = random.choice(data)
    print(f"Against A: {second_person['name']}, a {second_person['description']}, from {second_person['country']}")

    user_guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    if first_person['follower_count'] > second_person['follower_count'] and user_guess == 'a':
        game_score += 1
    elif first_person['follower_count'] < second_person['follower_count'] and user_guess == 'b':
        game_score += 1
    else:
        os.system('cls')
        print(logo)
        print(f"Sorry, that's wrong. Final score: {game_score}")
        break
