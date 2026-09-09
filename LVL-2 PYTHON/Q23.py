# Write a program to get a number from the user and print the total number of single-digit perfect square numbers in the number.
num = input()
count = 0

for digit in num:
    if digit in "149":
        count += 1

print(count)