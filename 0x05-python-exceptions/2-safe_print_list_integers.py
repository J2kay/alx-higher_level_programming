#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    i = 0
    try:
        while count < x:
            try:
                print("{:d}".format(my_list[i]), end="")
                count += 1
            except (ValueError, TypeError):
                pass
            except IndexError:
                break
            i += 1
        print()
    except Exception:
        print("An error occured")
    return count
