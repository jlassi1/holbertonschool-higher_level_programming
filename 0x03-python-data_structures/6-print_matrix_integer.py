#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):

    for k in range(len(matrix)):
        for m in range(len(matrix[k])):
            if m == len(matrix[k]) - 1:
                print("{:d}".format(matrix[k][m]), end="")
            else:
                print("{:d}".format(matrix[k][m]), end=" ")
        print()
