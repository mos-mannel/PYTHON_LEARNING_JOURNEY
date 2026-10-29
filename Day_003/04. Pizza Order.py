### EXERCISE INSTRUCTIONS:
# Build an automatic pizza order program based on a user's order and work out their final bill.
#Small pizza : $15
#medium pizza: $20
#large pizza: $25

#pepperoni for small pizza :  + $2
#pepperoni for medium or large pizza :  + $3
#extra cheese for any size is + $1
'''
print("Welcome to Python Pizza deliveries ! ")
size = input("What size of pizza do you want ?  S, M, or L \n")
add_pepperoni = input("Do you want pepperoni? Y or N \n")
extra_cheese = input("Do you want extra cheese? Y or N \n")

if size == "S":
    if add_pepperoni == "Y":
        if extra_cheese == "Y":
            print("The price is $ 18 ")
        elif extra_cheese == "N":
            print("The price is $17 ")
    elif add_pepperoni == "N":
        print("The price is $15")

elif size == "M":
    if add_pepperoni == "Y":
        if extra_cheese == "Y":
            print("The price is $ 24 ")
        elif extra_cheese == "N":
            print("The price is $ 23 ")
    elif add_pepperoni == "N":
        print("The price is $ 20")

elif size == "L":
    if add_pepperoni == "Y":
        if extra_cheese == "Y":
            print("The price is $ 29 ")
        elif extra_cheese == "N":
            print("The price is $ 28 ")
    elif add_pepperoni == "N":
        print("The price is $ 25")


'''






### MY TUTOR'S SOLUTION:

print("Welcome to Python Pizza deliveries ! ")
size = input("What size of pizza do you want ?  S, M, or L \n")
add_pepperoni = input("Do you want pepperoni? Y or N \n")
extra_cheese = input("Do you want extra cheese? Y or N \n")

bill = 0
if size == "S":
    bill += 15
elif size == "M":
    bill += 20
else :
    bill += 25

if add_pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill +=  3

if extra_cheese == "Y":
    bill =+ 1

print(f"The total bill is ${bill}")
