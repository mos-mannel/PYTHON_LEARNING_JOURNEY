

### INSTRUCTIONS

#You are going to write a program that calculates the highest scores from a List of scores.
#You are not allowed to use the max() and the min()

student_scores = input("Input a list of student scores \n ").split(",")
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
highest_score = 0

for score in student_scores:
    if score > highest_score:
        highest_score = score
print(f"The highest score in the list is {highest_score}.")