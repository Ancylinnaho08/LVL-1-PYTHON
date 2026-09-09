def digit_sum(num):
    hundred = num // 100
    tens = (num // 10) % 10
    ones = num % 10

    total = hundred + tens + ones
    return total


num = int(input())
print(digit_sum(num))