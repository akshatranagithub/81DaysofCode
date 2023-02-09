height = float(input("Enter the height in m: "))
weight = float(input("Enter the weight in kg: "))
bmi = round(weight/(height**2))

print("Your BMI is {bmi}")
if bmi<18:
    print(f"You are underweight")
elif bmi<25:
    print(f"You are normal weight")
elif bmi<30:
    print(f"You are overweight")
elif bmi<35:
    print("You are obese")
else:
    print("You are clinically obese")