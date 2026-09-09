def digit_sum(num):
    total = 0

    while num > 0:
        total = total + (num % 10)
        num = num // 10

    return total


num = int(input())
print(digit_sum(num))