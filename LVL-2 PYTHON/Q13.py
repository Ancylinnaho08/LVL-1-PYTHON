# Write a program to get a number from the user and print the reverse of that number.
num = int(input())
reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10

print(reverse)