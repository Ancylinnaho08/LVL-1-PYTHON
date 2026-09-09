def count_words(text):
    words = text.split()
    return len(words)


text = input()
print(count_words(text))