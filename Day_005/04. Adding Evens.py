
### INSTRUCTION

# You are going to write a program that calculates the sum of all the even numbers from 1 to 100 including 1 and 100
#Important, there should only be 1 print statement in your console output.
# It should just print the final total and not every step of the calculation.

sum_even = 0
for n in range(2, 101, 2):
    sum_even += n
print(sum_even)

total2 = 0
for number in range(1, 101):
    if number % 2 == 0:
        total2 += number
print(total2)