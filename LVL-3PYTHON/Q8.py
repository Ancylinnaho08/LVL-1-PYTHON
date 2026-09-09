#Get a number from user and check whether its digits are in ascending order.
def check_ascending(num):
    previous = num % 10
    num = num // 10

    while num > 0:
        digit = num % 10

        if digit >= previous:
            return "No"

        previous = digit
        num = num // 10

    return "Yes"


num = int(input())
print(check_ascending(num))