#Write a program to get a number from the user. If the first digit is even, print the same number. If the first digit is odd, subtract 1 from the first digit and print the number.
num = input()

first = int(num[0])

if first % 2 == 0:
    print(num)
else:
    print(str(first - 1) + num[1:])