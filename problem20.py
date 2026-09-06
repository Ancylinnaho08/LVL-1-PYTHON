# Get a three-digit number from user and make the ten's digit as 0, then print it.
num = int(input())
result = (num // 100) * 100 + (num % 10)
print(result)