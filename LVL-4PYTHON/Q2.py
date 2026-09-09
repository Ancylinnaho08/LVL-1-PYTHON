def tens_digit(num):
    return (num // 10) % 10


num = int(input())
result = tens_digit(num)

print(result)