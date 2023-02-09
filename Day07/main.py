import random

from hangman_words import word_list

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

guessed = []
from hangman_art import *

print(logo)
print(f'Pssst, the solution is {chosen_word}.')

display = ['_'] * word_length

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    guessed.append(guess)
    if guess in display or guess in guessed:
        print(f"You have already guessed the letter {guess}")

    else:
        for position in range(word_length):
            letter = chosen_word[position]
            if letter == guess:
                display[position] = letter

    if guess not in chosen_word:
        print(f"You guessed the wrong letter: {guess}")
        print("You lose a life")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You LOSE!")

    print(f"{''.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You WIN!")

    print(stages[lives])
