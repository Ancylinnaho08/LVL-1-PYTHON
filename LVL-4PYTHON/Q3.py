def ones_digit(num):
    digit = num % 10
    return digit


num = int(input())
print(ones_digit(num))