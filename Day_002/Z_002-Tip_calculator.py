
### TIP CALCULATOR

print("Welcome to the tip calculator \n")
bill = float(input("what was the total bill \n"))
tip_percentage = float(input("what percentage would you like to give, 10, 12, or 15 ? \n"))
num_people = int(input("How many people to split the bill? \n"))

tip_bill = ((tip_percentage / 100) * bill)
total_bill = (tip_bill + bill)
amount_per_head = (total_bill / num_people)

print(f"Each person should pay: {round(amount_per_head, 1)}")



