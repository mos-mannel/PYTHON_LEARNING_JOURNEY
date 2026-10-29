
### INSTRUCTION

# You are going to write a program which will select a random name from a list of names.
# The person selected will have to pay for everybody's food bill.

import random

test_seed = int(input("Create a seed number: \n "))
random.seed(test_seed)
nameAsCVS = input("Give me everybody's names, separated by comma: \n")
names = nameAsCVS.split(", ")
#print(names)

who_pays = random.choice(names)
print(f"{who_pays} is going to pay for everyone")
