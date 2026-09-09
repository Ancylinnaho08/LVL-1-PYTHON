# Get a three-digit number from user and print sum the digits.
num = int(input())
result = (num // 100) + ((num // 10) % 10) + (num % 10)
print(result)