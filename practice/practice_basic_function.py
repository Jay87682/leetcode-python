#!/usr/bin/python3
###### User defined functions ######

""" Functions are first-class functions """
## Function could be assigned to a variable
# def my_func(test):
#     return "test string: " + test
#
# my_func_var = my_func
# print(my_func_var("hello"))

## Function in Function (inner function)
# def my_func(test):
#     def prefix_msg():
#         return "test string: "

#     return prefix_msg() + test

# print(my_func("hello"))

# def add1(x):
#   def add2(y):
#     return x+y
#   return add2
# nest_add=add1(1)
# print(nest_add(3))

## Functions as parameters
# def my_func(test):
#     return "test string : " + test
#
# def call_func(func):
#     t = "hello"
#     return func(t)
#
# print(call_func(my_func))


## Functions can return(generate) other Functions
# def compose_my_func():
#     def my_func(test):
#         return "test string: " + test
#     return my_func
#
# my_func_var = compose_my_func()
# print(my_func_var("test"))

### Override Function ###

"""Python don't support functions overloading"""

## Late one will replace previous one
# def sum(a, b):
#     return a+b
#
# def sum(a, b, c):
#     return a+b+c
#
# print(sum(10, 20, 30))
# print(sum(10, 20))  ##Error!!

## Trick method to simulte function overload
# def sum(a, b):
#     return a+b
#
# def sum(a, b, c = 0):
#     return a+b+c
#
# print(sum(10, 20, 30))
# print(sum(10, 20))

""" Function with the mutable parameters """
# def append_list(element, arr = []):
#     print("id is : " + str(id(arr)))
#     arr.append(element)
#     return arr
# ## Pass the list parameter (second parameter)
# print(append_list(10, [1, 2, 3]))
#
# ##Following invoke will use the same list object
# print(append_list(10))
# print(append_list(20))
# print(append_list(30))

""" Function with arbitrary parameters """
# def sum(*numbers):
#     total = 0
#     for number in numbers:
#         total += number
#     return total
#
# print(sum(1, 2))
# print(sum(1, 2, 3))
# print(sum(1, 2, 3, 4))

""" Function with the tuple parameter set """
# def sum(a, b, c):
#     return a+b+c
# paras = (1, 2, 3)
# print(sum(*paras))


""" Get the memory consumption
    * Consumption directly attributed to the object is accounted for
    * Not the memory consumption of objects it refers to
    * call the __sizeof__ methods and adds an additional garbage
      collector overhead
"""
# import sys
# print(sys.getsizeof(())) #tuple
#
# print(sys.getsizeof({})) #dic
# print(sys.getsizeof(set())) #set
# print(sys.getsizeof([])) #list
# print(sys.getsizeof("")) #string
# print(sys.getsizeof(1235)) #string

""" Iterator objects def. """
## In python2
# print([1, 2, 3].__iter__().next())
## In python3
# print([1, 2, 3].__iter__().__next__())

# class NumberGenerator:
#     class Iterator:
#         def __init__(self, length):
#             self.length = length
#             self.number = -1
#         def __next__(self):
#             self.number = self.number + 1
#             if self.number == self.length:
#                 raise StopIteration
#             return self.number
#         def next(self):
#             self.number = self.number + 1
#             if self.number == self.length:
#                 raise StopIteration
#             return self.number
#
#     def __init__(self, length):
#         self.length = length
#
#     def __iter__(self):
#         return NumberGenerator.Iterator(self.length)
#
# print(dir(NumberGenerator(10).__iter__()))
# test = NumberGenerator(10)
# for n in NumberGenerator(10):
#     print(test.__iter__())
#     print(n)
