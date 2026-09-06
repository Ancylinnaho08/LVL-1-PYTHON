# Get a two-digit number from user and subtract 5 from that number if the sum of the digits of the number is odd, then print the result. Do not use "if".
num = int(input())
tens = num // 10
ones = num % 10
result = num - ((tens + ones) % 2) * 5
print(result)