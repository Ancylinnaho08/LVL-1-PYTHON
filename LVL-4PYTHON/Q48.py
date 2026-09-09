def adjust_carry(array):
    for i in range(len(array) - 1, 0, -1):
        if array[i] >= 10:
            carry = array[i] // 10
            array[i] = array[i] % 10
            array[i - 1] = array[i - 1] + carry

    return array


array = [6, 12, 3, 15, 7]
print(*adjust_carry(array))