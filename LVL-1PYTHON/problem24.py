# Get a three-digit number from user and subtract 5 from that number if one's digit and hundred's digit are the same, then print the result. Do not use "if".
num = int(input())
hundred = num // 100
ones = num % 10
result = num - (hundred == ones) * 5
print(result)