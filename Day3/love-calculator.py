print("Welcome to the Love Calculator")
name1 = input("Enter the first name: ")
name2 = input("Enter the second name: ")

combined_string = name1 + name2
lower_case_string = combined_string.lower()

t = lower_case_string.count('t')
r = lower_case_string.count('r')
u = lower_case_string.count('u')
e = lower_case_string.count('e')

l = lower_case_string.count('l')
o = lower_case_string.count('o')
v = lower_case_string.count('v')
e = lower_case_string.count('e')

true = t + r + u + e
love = l + o + v + e

love_score = int(str(true) + str(love))

print(f"Your score is {love_score}%")
if love_score < 10 or love_score > 90:
    print("You go together like coke and mentos")
elif 40 <= love_score <= 50:
    print("You are alright together")
