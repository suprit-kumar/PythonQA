"""Python Program to find sum of array"""

# def sum_of_array(arr):
#     # return sum(arr)
#     sum = 0
#     for i in arr:
#         sum = sum +i
#     return sum
# output = sum_of_array([5,6,7])
# print('The sum of the array -->',output)

"""Python Program to find largest element in an array"""

# def find_largest_number(arr):
#     arr.sort()
#     return  arr[-1]
#
# output = find_largest_number([10,7,9,16,5])
# print("The largest number is -->",output)



"""Python Program for array rotation"""

# arr = [1, 2, 3, 4, 5, 6, 7], d = 2, n =7

# def array_rotation():
#     arr = [1, 2, 3, 4, 5, 6, 7]
#     d, n = 2, 7
#     temp = []
#     rest_arr = []
#     for i in arr:
#         if i == d or i < d:
#             temp.append(i)
#         else:
#             rest_arr.append(i)
#
#     rest_arr.extend(temp)
#     print('rest arry =', rest_arr)
#
# array_rotation()


"""Python Program to Split the array and add the first part to the end"""

# def split_array():
#     arr = [12, 10, 5, 6, 52, 36]
#     k = 2  # index
#     first_arr = arr[:2:]
#     second_arr = arr[2::]
#     second_arr.extend(first_arr)
#     print(second_arr)
# split_array()