#Get a number from user and check whether the sum of digits is 14, then print the result.
def check_sum(num):
    sum = 0

    while num > 0:
        sum = sum + (num % 10)
        num = num // 10

    if sum == 14:
        print("Sum of Digits is 14")
    else:
        print("Sum of Digits is not 14")

num = int(input())
check_sum(num)