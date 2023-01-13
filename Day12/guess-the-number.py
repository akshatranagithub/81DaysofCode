import random

print("Welcome the number guessing game")
print("I am thinking of a number between 1 and 100")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

if difficulty == 'easy':
    attempts = 10
elif difficulty == 'hard':
    attempts = 5
else:
    attempts = 0

number = random.randint(1, 100)

while attempts > 0:
    print(f"You have {attempts} attempts remaining to guess the number")
    guess = int(input("Make a guess: "))

    if guess == number:
        print("You have guessed the number, You won!")
        break
    elif guess < number:
        print("Too low")
    else:
        print("Too high")

    attempts -= 1

    if attempts == 0:
        print("You have run out of guesses, You lose!")
