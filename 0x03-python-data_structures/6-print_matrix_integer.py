#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    n = len(matrix)
    m = len(matrix[0])
    for i in range(0, n):
        for j in range(0, m):
            if j != m - 1:
                print("{}".format(matrix[i][j]), end=' ')
            else:
                print("{}".format(matrix[i][j]), end='')
        print("")
