def array_to_string(array):
    result = ""

    for num in array:
        result = result + str(num)

    return result


array = list(map(int, input().split()))

print(array_to_string(array))