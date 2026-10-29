'''
height = int(input("What is your height ? \n"))
age = int(input("What is your age  ? \n"))
want_photos = str(input("Do you want photos ? Y or N \n"))

bill = 0

if height > 120:
    if age < 12:
        bill += 5
    elif 12 <= age < 18:
        bill += 7
    elif age > 18:
        bill += 12
    elif 45 <= age <= 55:
        bill += 0
else:
    print("You can not ride")

if want_photos == "Y":
    bill += 3
print(f"Your total bill is  ${bill}")
'''
### MY TUTOR'S SOLUTION:

height = int(input("What is your height ? \n"))
bill = 0
if height >= 120:
   print("You can ride the rollercoaster!")
   age = int(input("what is your age ?  \n"))
   if age < 12:
      bill = 5
      print("Child tickets are $5.")
   elif age > 18:
      bill = 7
      print("Youth tickets are $7")
   elif 45 <= age <= 55:
      print("Everything is going to be ok. Have a free ride on us!")
   else:
      bill = 12
      print("Adult tickets are $12.")


wants_photo = input("Do you want a photo taken? Y or N  \n")
if wants_photo == "Y":
   bill += 3
print(f"Your final bill is ${bill}")


