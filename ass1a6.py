#Write a program to calculate sum of first and last digit of a number. 
num = int(input("Enter a number: "))

last_digit = num % 10

first_digit = num
while first_digit >= 10:
    first_digit //= 10

sum_digits = first_digit + last_digit

print(f"First digit: {first_digit}")
print(f"Last digit: {last_digit}")
print(f"Sum of first and last digit: {sum_digits}")
