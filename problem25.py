# Get a four-digit number from user and subtract 5 from that number if ten's digit position and hundred's digit position are the same, then print the result. Do not use "if".
num = int(input())
hundred = (num // 100) % 10
tens = (num // 10) % 10
result = num - (hundred == tens) * 5
print(result)