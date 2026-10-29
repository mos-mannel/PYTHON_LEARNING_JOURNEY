### Exercise:
# Write a program that adds the digits in a 2-digit number. eg: if the input was 35, then the output should be 3+5 = 8

two_digit_number = input("Type a two digit number:  \n")

first_digit = two_digit_number[0]
second_digit = two_digit_number[1]

new_first_digit = (int(first_digit))
new_second_digit = (int(second_digit))

print(new_first_digit + new_second_digit)


