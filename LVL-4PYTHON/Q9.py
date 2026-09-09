def digit_sum(num):
    tens = num // 10
    ones = num % 10

    total = tens + ones
    return total


num = int(input())
print(digit_sum(num))