def find_length(text):
    count = 0

    for character in text:
        count = count + 1

    return count


text = input()
print(find_length(text))