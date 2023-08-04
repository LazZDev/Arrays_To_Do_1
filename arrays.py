# Shuffle
import random


def shuffle(arr):
    for i in range(len(arr) - 1, 0, -1):
        j = random.randint(0, i)
        arr[i], arr[j] = arr[j], arr[i]


my_array = [1, 2, 3, 4, 5]
shuffle(my_array)
print(my_array)


# Skyline Heights
def skyline_heights(arr):
    visible_buildings = []
    max_height = 0
    for height in reversed(arr):
        if height > max_height:
            visible_buildings.append(height)
            max_height = height
    return list(reversed(visible_buildings))


buildings = [-1, 1, 1, 7, 3]
print(skyline_heights(buildings))

buildings2 = [0, 4]
print(skyline_heights(buildings2))


# Zip It
def zip_arrays(arr1, arr2):
    result = []
    length = max(len(arr1), len(arr2))

    for i in range(length):
        if i < len(arr1):
            result.append(arr1[i])
        if i < len(arr2):
            result.append(arr2[i])

    return result


array1 = [4, 15, 100]
array2 = [10, 20, 30, 40]
print(zip_arrays(array1, array2))
