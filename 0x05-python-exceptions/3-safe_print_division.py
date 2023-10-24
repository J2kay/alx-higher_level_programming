#!/usr/bin/python3
def safe_print_division(a, b):
    value = None
    try:
        value = a / b
    except ZeroDivisionError:
        value = None
    finally:
        if value is not None:
            print("Inside result: {:.1f}".format(value))
        else:
            print("Inside result: {:s}".format(str(value)))
    return value
