print("Welcome to the BMI Calculator")
weight1 = int(input("What is your weight?"))

weight = 85
height = 1.85
bmi = weight / (height ** 2)



if bmi < 18.5:
    print("underweight")
elif 18.5 <= bmi <= 25:
    print("normal weight")
else:
    print("overweight")