def reverse_number(num):
    thousand = num // 1000
    hundred = (num // 100) % 10
    tens = (num // 10) % 10
    ones = num % 10

    reverse = (ones * 1000) + (tens * 100) + (hundred * 10) + thousand
    return reverse


num = int(input())
print(reverse_number(num))