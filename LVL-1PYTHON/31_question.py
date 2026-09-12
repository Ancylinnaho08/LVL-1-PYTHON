# Get a three-digit number from user. If the sum of the digits is less than 10, then print the sum, otherwise add the digits of the sum and continue until the result is a single digit.
num = int(input())

sum = (num // 100) + ((num // 10) % 10) + (num % 10)

while sum >= 10:
    sum = (sum // 10) + (sum % 10)

print(sum)