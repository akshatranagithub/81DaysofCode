print("Welcome to the Treasure Island")
print("Your mission is to find the treasure")

choice1 = input("You are at a crossroad. Where do you want to go? Type 'left' or 'right': ").lower()

if choice1 == 'left':
    choice2 = input("You have come to a lake. There is an island in the middle of the lake. Type 'wait' to wait for "
                    "the boat. Type 'swim' to swim across: ").lower()
    if choice2 == 'wait':
        choice3 = input("You arrive at the island unharmed. There is a house with 3 doors. Red, yellow and blue. "
                        "Which color do you want to choose: ").lower()
        if choice3 == 'red':
            print("The room is full of fire. GAME OVER!")
        elif choice3 == 'yellow':
            print("You found the treasure. YOU WIN!")
        elif choice3 == 'blue':
            print("You enter a room of beasts. GAME OVER!")

    else:
        print("You got attacked by an angry trout. GAME OVER!")
else:
    print("You fell into a hole. GAME OVER!")

