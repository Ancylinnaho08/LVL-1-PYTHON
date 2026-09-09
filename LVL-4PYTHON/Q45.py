def reverse_number(text):
    reverse = ""

    for digit in text:
        reverse = digit + reverse

    return reverse


text = input()
print(reverse_number(text))