#Day 3

# #Code exercise Odd or Even
# number = int(input("Which number do you want to check?: "))

# if number % 2 == 0:
#     print("This is an even number.")
# else:
#     print("This is an odd number.")

#Code exercise BMI 2.0
height = float(input("Enter your height in meters: "))
weight = float(input("Enter your weight in kilograms: "))
bmi = weight / (height ** 2)
if bmi < 18.5:
    bmi_adjective = "underweight"
elif bmi < 25:
    bmi_adjective = "a normal weight"
elif bmi < 30:
    bmi_adjective = "overweight"
elif bmi < 35:
    bmi_adjective = "obese"
else:
    bmi_adjective = "clinically obese"

print(f"Your BMI is {int(bmi)}, and you are {bmi_adjective}")
