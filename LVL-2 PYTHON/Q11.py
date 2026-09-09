# Write a program to get a number from the user and print the total number of digits in that number.
num = int(input())
count = 0

while num > 0:
    num = num // 10
    count = count + 1

print(count)