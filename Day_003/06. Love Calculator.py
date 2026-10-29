

#You are going to write a program that tests the compactibility between two people.

 ## GUIDE_:  Take both people's names and check for the number of times the letters in the word LOVE occurs.
# Then combine these numbers to make a 2-digit number.
# For the love scores less than 10 0r greater than 90, the message should be: "Your score is x, you go together like coke and mentos."
# For the love scores less between 40 and 50, the message should be: "Your score is y, you are alright together."
# otherwise, the message will be their score e.g.  " Your score is z"


print("Welcome to the Love Calculator! \n")
name1 = str(input("What is your name? \n")).lower()
name2 = str(input("What is their name? \n")).lower()

name = name1 + name2
length = (len(name))
a = name.count("l")
b = name.count("o")
c = name.count("v")
d = name.count("e")
total_num = int(a + b + c + d)

love_percent = int((total_num / length * 100))

if love_percent < 10 or love_percent > 90:
    print(f"Your score is {love_percent}%, You go together like coke and mentos")
elif 40 < love_percent < 50:
    print(f"Your score is {love_percent}%, you are alright together.")
else:
    print(f"Your score is {love_percent}%.")


