# Get two 2-digit numbers from user. If the sum of the numbers is less than 100, then print the sum, otherwise print the difference.
a, b = map(int, input().split())

if a + b < 100:
    print(a + b)
else:
    print(abs(a - b))