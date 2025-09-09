#!/usr/bin/python3
def raise_exception_msg(message=""):
    raise NameError(message)
try:
    raise_exception_msg("a message")
except NameError as err:
    print(err)
