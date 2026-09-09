def convert_to_array(text):
    array = []

    for digit in text:
        array.append(int(digit))

    return array


text = input()
print(convert_to_array(text))