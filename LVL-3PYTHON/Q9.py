#Get a two-digit number from user and swap the digits.
def swap_digits(num):
    tens = num // 10
    ones = num % 10

    result = ones * 10 + tens

    return result


num = int(input())
print(swap_digits(num))