# Get two 3-digit numbers from user. Print the difference between the one's digit and hundred's digit of the number whose ten's digit is bigger than the other number's ten's digit.
a, b = map(int, input().split())

tens_a = (a // 10) % 10
tens_b = (b // 10) % 10

if tens_a > tens_b:
    num = a
else:
    num = b

hundred = num // 100
ones = num % 10

print(abs(ones - hundred))