#Write a program to print the total count of numbers less than 100000 whose sum of digits is 14.
count = 0

for i in range(100000):
    num = i
    sum = 0

    while num > 0:
        sum += num % 10
        num //= 10

    if sum == 14:
        count += 1

print(count)