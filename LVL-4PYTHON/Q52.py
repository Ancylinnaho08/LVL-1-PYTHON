def find_substring(text, substring):
    position = text.find(substring)

    if position != -1:
        return position + 1
    else:
        return -1


text = input()
substring = input()

print(find_substring(text, substring))