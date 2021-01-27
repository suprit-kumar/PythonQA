"""Python program to interchange first and last elements in a list"""

# def interchange1Elements(arr):
#     size = len(arr)
#     # Swaap array
#     temp = arr[0]
#     arr[0] = arr[size - 1]
#     arr[size - 1] = temp
#
#     return arr
# arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# swap = interchange1Elements(arr)
# print('After swapping list -->',swap)


"""Python program to swap two elements in a list"""

"""Python | Ways to find length of list"""

# def find_length():
#     test_list = [1, 4, 5, 7, 8]
#     print("1.length of list ==>",len(test_list))
#     count = 0
#     for i in test_list:
#         count+=1
#     print("2.length of list ==>",count)
#
# find_length()


"""Python | Ways to check if element exists in list"""

# def check_element(arr, e):
#     # if e in arr:
#     #     print("1.Element exist in list")
#     # else:
#     #     print("2.Element not exist in list")
#     for i in arr:
#         if i == e:
#             print("Exist")
#     print("Not exist")
# test_list = [1, 4, 5, 7, 8]
# n = 4
# check_element(test_list, n)


"""Different ways to clear a list in Python"""

# def clear_list():
#     list1 = [1, 2, 3]
#     # list1[:]=[]
#     # list1.clear()
#     print(list1)
#
# clear_list()


"""Python | Reversing a List"""

# def reverse_list():
#     list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#     print(list1[::-1])
#     list1.reverse()
#     print(list1)
# reverse_list()

"""Python program to find sum of elements in list"""

# def sum_of_list(arr):
#     try:
#         total = 0
#         for i in arr:
#             total = total + i
#         return total
#     except:
#         return "Invalid list (List element should be integer and float)"
#
# my_list = [1,2,3,4,5,6,7,8,9,10]
# ans = sum_of_list(my_list)
# print(ans)

"""Python | Multiply all numbers in the list"""

# def multiplication_of_list(arr):
#     try:
#         total = 1
#         for i in arr:
#             if type(i) is int or type(i) is float:
#                 total = total * i
#         return total
#     except:
#         return "Invalid list (List element should be integer and float)"
#
# my_list = [1,2,3,4,5,6,7,8,9,10]
# ans = multiplication_of_list(my_list)
# print(ans)

""""Python program to find smallest number in a list"""

# def find_smallest(arr):
#     minimum = arr[0]
#     for i in range(len(arr)):
#         if arr[i] < minimum:
#             minimum = arr[i]
#     return minimum
# my_list = [22, 15, 84, 27, 19, 100, 5, 222, 56, 12, 6]
# ans = find_smallest(my_list)
# print(ans)

"""Python program to find largest number in a list"""

# def find_largest(arr):
#     maximum = arr[0]
#     for i in range(len(arr)):
#         if arr[i] > maximum:
#             maximum = arr[i]
#     return maximum
# my_list = [22, 15, 84, 27, 19, 100, 5, 222, 56, 12, 6]
# ans = find_largest(my_list)
# print(ans)
