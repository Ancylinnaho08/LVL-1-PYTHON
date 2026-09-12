# Write a program to get two numbers from the user and print the LCM of those numbers.
a, b = map(int, input().split())

if a > b:
    lcm = a
else:
    lcm = b

while True:
    if lcm % a == 0 and lcm % b == 0:
        print(lcm)
        break
    lcm += 1