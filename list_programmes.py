"""Python program to interchange first and last elements in a list"""


def interchange1Elements(arr):
    first_index = arr[0]
    last_index = arr[-1]
    arr.remove(arr[0])
    arr.remove(arr[-1])
    arr.insert(arr[0], last_index)
    arr.insert(arr[-1], first_index)
    print(arr)


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
interchange1Elements(arr)
