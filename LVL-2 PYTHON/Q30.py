# Write a program to get two numbers from the user and print the HCF of those numbers.
a, b = map(int, input().split())

while b != 0:
    a, b = b, a % b

print(a)