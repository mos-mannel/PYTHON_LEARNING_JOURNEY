### EXERCISE INSTRUCTIONS

# Write a program that works out whether if a given number is odd or even number.
# Even numbers can be divided by 2 with no remainder.


number = int(input("Which number do you want to check ? \n" ))
if number % 2 == 0:
    print("This number is even")
else:
    print("This number is odd")

