# Get a four-digit number from user and only reverse the first two digits of the number, then print the number.
num = int(input())
a = num // 1000
b = (num // 100) % 10
c = (num // 10) % 10
d = num % 10

result = b * 1000 + a * 100 + c * 10 + d
print(result)