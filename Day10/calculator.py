from art import logo

print(logo)


def add(first, second):
    return first + second


def sub(first, second):
    return first - second


def mul(first, second):
    return first * second


def div(first, second):
    return first / second


answer = 0
choice = 'y'
first = float(input("Enter the first number: "))

while choice == 'y':
    print("Choose an operation (+ - * /)")
    op = input("Enter the operation: ")
    next = float(input("Enter the next number: "))

    if op == '+':
        answer = add(first, next)
    elif op == '-':
        answer = sub(first, next)
    elif op == '*':
        answer = mul(first, next)
    elif op == '/':
        answer = div(first, next)
    else:
        print("Wrong input operation")
        continue

    print(f"{first} {op} {next} = {answer}")
    choice = input(f"Type 'y' to continue calculating with {answer} or 'n' to exit: ")

    if choice == 'y':
        first = answer
