# Get a two-digit number from user and make the ten's digit 1, then print it.
num = int(input())
result = 10 + (num % 10)
print(result)