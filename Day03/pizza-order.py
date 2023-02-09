print("Welcome to the Python Pizza Deliveries")
size = input("What size of pizza do you want? S,M or L: ")
add_pepperoni = input("Do you want pepperoni? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

total = 0
if size == 'S':
    total += 15
elif size == 'M':
    total += 20
elif size == 'L':
    total += 25

if add_pepperoni == 'Y' and size == 'S':
    total += 2
elif add_pepperoni == 'Y' and size == 'M' or size == 'L':
    total += 3

if extra_cheese == 'Y':
    total += 1

print(f"Your final bill is ${total}")