### Exercise:
# Write a program that calculates the Body Mass Index (BMI) from a user's weight and height.
#The BMI is a measure of someone's weight taking into account their height. e.g. if a tall person and a short person both weigh the same amount, the short person is usually more overweight.
# The BMI is calculated by dividing a person's weight (in kg) by the square of their height (in m):



height = float(input("What is your height in cm ? \n"))
weight = float(input("What is your weight in kg ? \n "))

BMI = int(weight / (height **2))

result = f"Your Body Mass Index is {BMI} "

print(result)



