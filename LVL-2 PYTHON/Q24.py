# Write a program to get a number from the user and print the total number of two-digit perfect square numbers in the number.
num = input()
count = 0

for i in range(len(num) - 1):
    two_digit = int(num[i:i+2])

    if two_digit in [16, 25, 36, 49, 64, 81]:
        count += 1

print(count)