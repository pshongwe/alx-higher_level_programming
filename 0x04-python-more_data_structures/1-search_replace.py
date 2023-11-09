#!/usr/bin/python3

def search_replace(my_list, search, replace):
    new = []
    for e in my_list:
        if e == search:
            new.append(replace)
        else:
            new.append(e)
    return new
