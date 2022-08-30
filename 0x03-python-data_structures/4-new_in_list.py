#!/usr/bin/python3
def no_c(my_string):
    my_string_list = list(my_string)
    new_string = [l for l in my_string_list if l != 'c' and l != 'C']
    return "".join(new_string)
