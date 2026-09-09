# Get a three-digit number from user and make the one's digit as 2, then print it.
num = int(input())
result = (num // 10) * 10 + 2
print(result)