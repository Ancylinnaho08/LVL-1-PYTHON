def find_positions(text, character):
    positions = []

    for i in range(len(text)):
        if text[i] == character:
            positions.append(i + 1)

    return positions


text = input()
character = input()

positions = find_positions(text, character)

print(*positions, sep=", ")