"""Python program to add two numbers"""

# def add_two_number(a,b):
#     return a+b
# sum = add_two_number(10,5)
# print('sum of two numbers -->',sum)

"""Maximum of two numbers in Python"""
# def find_maximum_btn_two_numbers(a,b):
#     if a > b:
#         return a
#     else:
#         return b
#
# maximum = find_maximum_btn_two_numbers(10,12)
# print('maximum between two -->',maximum)


"""Python Program for factorial of a number"""
# def find_factorial(num):
#    factorial = 1
#    for i in range(1,num+1):
#        factorial  = factorial *i
#    return factorial
#
# fact = find_factorial(4)
# print("Factorial of the number is -->",fact)


"""Python Program for simple interest"""
# Simple Interest = (P x T x R)/100
# Where,
# P is the principle amount
# T is the time and
# R is the rate

# def find_simple_interest(p,t,r):
#     simple_interest = (p*t*r)/100
#     return simple_interest
#
# interest = find_simple_interest(3000,7,1)
# print('simple interest is ->',interest)

"""Python Program for compound interest"""

# A = P(1 + R/100) t
# Compound Interest = A – P
# Where,
# A is amount
# P is principle amount
# R is the rate and
# T is the time span

# def compound_interest(p,r,t):
#     amount =p * (pow((1 + r / 100), t))
#     ci = amount - p
#     return ci
#
# ci = compound_interest(10000, 10.25, 5)
# print('ci -->',ci)


"""Python Program for Program to find area of a circle"""
# Area = pi * r2
# where r is radius of circle
# def find_area_of_circle(r):
#     pi = 3.142
#     area = pi*(r*r)
#     return area
#
# circle_area = find_area_of_circle(5)
# print(f"area of circle {circle_area}.")

"""Python program to print all Prime numbers"""

# def prime_numbers(n):
#     while n > 1:
#         for i in range(2, n):
#             if n % i == 0:
#                 break
#         else:
#             print(n)
#         n-=1
# prime_numbers(20)


"""Python program to check whether a number is Prime or not"""
# def check_prime(n):
#     for i in range(2,n):
#         if n%i == 0:
#             print('Not a prime number')
#             break
#     else:
#         print('This is a prime number')
#
# check_prime(7)


"""Program to print ASCII Value of a character"""

# def print_ascii(element):
#     print("The ASCII value of '" + element + "' is " ,ord(element))
#
# print_ascii('g')

"""Python Program for Sum of squares of first n natural numbers"""
# def sum_of_natural_number_squares(n):
#     sum = 0
#     for i in range(1,n+1):
#         sum += i*i
#     print(sum)
# sum_of_natural_number_squares(4)

"""Python Program for cube sum of first n natural numbers"""

# def sum_of_natural_number_cube(n):
#     sum = 0
#     for i in range(1, n + 1):
#         sum += i * i * i
#     print(sum)
#
#
# sum_of_natural_number_cube(4)
