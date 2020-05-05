#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    k = 0
    m = 0
    if len(matrix) != 0:
        for k in range(len(matrix)):
            for m in range(len(matrix[k])):
                if m == len(matrix[k]) - 1:
                    print("{}".format(matrix[k][m]), end="")
                else:
                    print("{}".format(matrix[k][m]), end=" ")
            print()

