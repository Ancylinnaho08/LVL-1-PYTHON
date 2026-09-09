def reverse_number(num):
    tens = num // 10
    ones = num % 10

    reverse = (ones * 10) + tens
    return reverse


num = int(input())
print(reverse_number(num))