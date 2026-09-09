def remove_zeroes(text):
    result = text.lstrip('0')

    if result == "":
        result = "0"

    return result


text = input()
print(remove_zeroes(text))