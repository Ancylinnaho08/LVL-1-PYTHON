# Write a program to get a number from the user and print whether that number is prime or not.
num = int(input())
count = 0

for i in range(1, num + 1):
    if num % i == 0:
        count = count + 1

if count == 2:
    print("Prime")
else:
    print("Not Prime")