# Get two 2-digit numbers from user. Print the sum of digits of the biggest number.
a, b = map(int, input().split())

big = max(a, b)
result = (big // 10) + (big % 10)

print(result)