def add_arrays(a, b):
    length = max(len(a), len(b))
    result = [0] * length

    for i in range(length):
        if i < len(a):
            result[i] = result[i] + a[i]

        if i < len(b):
            result[i] = result[i] + b[i]

    return result


a = [1, 2, 3]
b = [4, 5, 6]

print(add_arrays(a, b))