#Write a program to get three numbers from the user and print the LCM of those numbers.
a, b, c = map(int, input().split())

if a > b and a > c:
    lcm = a
elif b > c:
    lcm = b
else:
    lcm = c

while True:
    if lcm % a == 0 and lcm % b == 0 and lcm % c == 0:
        print(lcm)
        break
    lcm += 1