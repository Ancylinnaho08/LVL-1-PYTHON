# Write a program to get a number from the user and print the sum of all digits.
num = int(input())
sum = 0

while num > 0:
    digit = num % 10
    sum = sum + digit
    num = num // 10

print(sum)