def digit_sum(num):
    total = 0

    while num > 0:
        digit = num % 10
        total = total + digit
        num = num // 10

    return total


num = int(input())
print(digit_sum(num))