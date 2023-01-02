print("Welcome to the tip calculator")

total_bill = float(input("What was the total bill? ₹"))
number_of_people = int(input("How many people to split the bill? "))
tip_percentage = int(input("What percentage tip would you like to give? 10, 12 or 15? "))

refactored_bill = total_bill + (total_bill*tip_percentage)/100
pay_for_each_person = refactored_bill/number_of_people
print(f"Each person should pay: ₹{round(pay_for_each_person,2)}")
