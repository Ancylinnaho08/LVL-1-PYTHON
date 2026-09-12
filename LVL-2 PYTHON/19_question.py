# Write a program to get a 4-digit number from the user and print whether the middle two digits form a prime number.
num = int(input())

middle = (num // 10) % 100

count = 0

for i in range(1, middle + 1):
    if middle % i == 0:
        count += 1

if count == 2:
    print("Prime")
else:
    print("Not Prime")