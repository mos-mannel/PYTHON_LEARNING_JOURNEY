### EXERCISE INSTRUCTIONS

#Write a program that works out whether if a particular year is a leap year.

leap_year = int(input("Enter the year: \n"))

if leap_year % 4 == 0:
    if leap_year % 100 == 0:
        if leap_year % 400 == 0:
            print("It's a leap year")
        else:
            print("It's NOT a leap year")
    else:
        print("It's a leap year")
else:
    print("It's NOT a leap year")



