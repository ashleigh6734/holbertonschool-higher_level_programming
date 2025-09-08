#!/usr/bin/python3
a = 89
b = 10
a, b = b, a
print("a={:d} - b={:d}".format(a, b))
# a, b = b, a is the Pythonic way to swap values
# The following is a more traditional way to swap values
# temp = a
# a = b
# b = temp
# print("a={:d} - b={:d}".format(a, b))
