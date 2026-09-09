# Get a number from user and subtract 5 from that number if the number's ten's position digit is odd, then print the result. Do not use "if".
num = int(input())
tens = (num // 10) % 10
result = num - (tens % 2) * 5
print(result)