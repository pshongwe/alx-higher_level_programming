#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    new_list = []
    for row in matrix:
        res = list(map(lambda x: x**2, row))
        new_list.append(res)
    return new_list
