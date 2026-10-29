
### INSTRUCTIONS

#You are going to write a program that calculates the average student height from a List of heights.
#Without using the sum() and len()

student_heights = input("Input a list of student heights \n ").split(",")
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

total_height = 0
for height in student_heights:
  total_height += height

student_number = 0
for height in student_heights:
  student_number += 1

Average_height = total_height / student_number

print(Average_height)


