#Get a number from user and check whether it is prime or not, then print the result.
def check_prime(num):
    count = 0

    for i in range(1, num + 1):
        if num % i == 0:
            count = count + 1

    if count == 2:
        print("Number is Prime")
    else:
        print("Number is not Prime")

num = int(input())
check_prime(num)