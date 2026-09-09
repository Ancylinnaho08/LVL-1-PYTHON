def reverse_number(num):
    hundred = num // 100
    tens = (num // 10) % 10
    ones = num % 10

    reverse = (ones * 100) + (tens * 10) + hundred
    return reverse


num = int(input())
print(reverse_number(num))