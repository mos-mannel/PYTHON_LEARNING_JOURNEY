###EXERCISE INSTRUCTIONS

#1. Write a program that interprets the Body Mass Index (BMI) based on a user's weight and height.
#It should tell them the interpretation of their BMI based on the BMI value.

   #a. Under 18.5, they are underweight
   #b. Over 18.5 but below 25, they have a normal weight
   #c. Over 25 but below 30, they are overweight
   #d. Over 30 but below 35 they are obese
   #c. Above 35, they are clinically obese

height = float(input("Enter your height in m: \n "))
weight = float(input("Enter your weight in kg: \n"))

BMI = weight / (height ** 2)

if BMI < 18.5:
    print("You are underweight")
elif BMI < 25:
    print("You have a normal weight")
elif BMI < 35:
    print("You are obese")
elif BMI >= 35:
    print("You are clinically obese")




