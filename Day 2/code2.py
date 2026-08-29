#BMI CODE

height = float(input("Enter height in meters (m):"))

weight = int(input("Enter weight in kilograms (kg):"))

bmi = weight / (height * height)
if bmi < 18.5:
    print(f"Your BMI is {bmi}, you are underweight.")
elif bmi < 25:
    print(f"Your BMI is {bmi}, you have a normal weight.")
elif bmi < 30:
    print(f"Your BMI is {bmi}, you are slightly overweight.")
elif bmi < 35:
    print(f"Your BMI is {bmi}, you are obese.")
else:
    print(f"Your BMI is {bmi}, you are clinically obese.")
#output
# Enter height in meters (m):1.80
# Enter weight in kilograms (kg):88
# Your BMI is 27.160493827160494, you are slightly overweight.