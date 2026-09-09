# Write a program to get a number from the user, print whether that number is prime, and check whether the sum of its digits is equal to 14.
num = int(input())

# Check prime
count = 0
for i in range(1, num + 1):
    if num % i == 0:
        count += 1

# Sum of digits
temp = num
sum = 0

while temp > 0:
    sum += temp % 10
    temp //= 10

if count == 2 and sum == 14:
    print("Prime & Sum of Digits is 14")
elif count != 2 and sum == 14:
    print("Not Prime but sum of digits is 14")
elif count == 2:
    print("Prime, but sum of Digits is not 14")
else:
    print("Not Prime & Sum of Digits is not 14")