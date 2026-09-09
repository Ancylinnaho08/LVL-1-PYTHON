def check_number(text):
    if text.isdigit():
        return "Valid Number"
    else:
        return "Not a Valid Number"


text = input()
print(check_number(text))