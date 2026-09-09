# Get a four-digit number from user and only reverse the last two digits of the number, then print the number.
num = int(input())
a = num // 1000
b = (num // 100) % 10
c = (num // 10) % 10
d = num % 10

result = a * 1000 + b * 100 + d * 10 + c
print(result)