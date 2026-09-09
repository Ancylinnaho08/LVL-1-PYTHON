# Write a program to get a number from the user and print whether the last two digits form a prime number.
num = int(input())
last_two = num % 100

count = 0

for i in range(1, last_two + 1):
    if last_two % i == 0:
        count += 1

if count == 2:
    print("Prime")
else:
    print("Not Prime")