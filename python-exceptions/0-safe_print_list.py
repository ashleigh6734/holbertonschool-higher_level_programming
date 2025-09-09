#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    print(my_list)
def catch_this():
    my_list = [1, 2, 3, 4, 5]

    for x in range(20):
        try:
            safe_print_list(my_list[x])
        except IndexError:
            safe_print_list(0)
catch_this()
