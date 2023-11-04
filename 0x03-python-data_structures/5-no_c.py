#!/usr/bin/python3
def no_c(my_string):
        result = ""
        for s in my_string:
                if s != 'c' and s != 'C':
                        result += s
        return result
