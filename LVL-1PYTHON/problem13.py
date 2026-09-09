# Get a two-digit number from user and print the reverse of the number.
num = int(input())
result = (num % 10) * 10 + (num // 10)
print(result)