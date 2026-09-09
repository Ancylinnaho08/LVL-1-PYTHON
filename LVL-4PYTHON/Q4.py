def tens_digit(num):
    digit = (num // 10) % 10
    return digit


num = int(input())
print(tens_digit(num))