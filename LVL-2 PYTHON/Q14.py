#Write a program to get a number from the user and interchange the first and last digits, then print the result.
num = input()

result = num[-1] + num[1:-1] + num[0]

print(result)