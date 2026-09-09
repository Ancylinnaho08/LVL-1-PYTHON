# Get two 3-digit numbers from user. Add the one's and hundred's digits of both numbers. Print the sum of all the digits of the number whose sum of one's and hundred's digits is bigger.
a, b = map(int, input().split())

sum_a = (a // 100) + (a % 10)
sum_b = (b // 100) + (b % 10)

if sum_a > sum_b:
    num = a
else:
    num = b

result = (num // 100) + ((num // 10) % 10) + (num % 10)

print(result)