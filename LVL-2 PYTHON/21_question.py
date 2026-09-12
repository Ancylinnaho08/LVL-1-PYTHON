#Write a program to get a number from the user and print the total number of digits that are odd.
num = int(input())
count = 0

while num > 0:
    digit = num % 10

    if digit % 2 != 0:
        count += 1

    num //= 10

print(count)