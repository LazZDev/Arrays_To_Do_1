# Shuffle
# In JavaScript, the Array object has numerous useful methods. It does not, however, contain a method that will randomize the order of an array’s elements. Let’s create shuffle(arr), to efficiently shuffle a given array’s values. Work in-place, naturally. Do you need to return anything from your function?
import random


def shuffle(arr):
    for i in range(len(arr) - 1, 0, -1):
        j = random.randint(0, i)
        arr[i], arr[j] = arr[j], arr[i]


my_array = [1, 2, 3, 4, 5]
shuffle(my_array)
print(my_array)


# Skyline Heights
# Lovely Burbank has a breathtaking view of the Los Angeles skyline. Let’s say you are given an array with heights of consecutive buildings, starting closest to you and extending away. Array [-1,7,3] would represent three buildings: first is actually out of view below street level, behind it is second at 7 stories high, third is 3 stories high (hidden behind the 7-story). You are situated at street level. Return array containing heights of buildings you can see, in order. Given [-1,1,1,7,3] return [1,7]. Given [0,4] return [4]. As always with challenges, do not use built-in array functions such as unshift().
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
# Create a standalone function that accepts two arrays and combines their values sequentially into a new array. Extra values from either array should be included afterward. Given [4,15,100] and [10,20,30,40], return new array containing [4,10,15,20,30,40,100].
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
