#!/user/bin/python3
"""
Program that device matrix by div
div must be number (int or float) and != 0
matris must be a matrix (list of lists) of integers/floats
and Each row of the matrix must have the same size
return new matrix each elements divided by div
"""


def matrix_divided(matrix, div):
    """
    function that return new matrix divided by div
    check if div a number (int or float)
    check if matrix is(list of lists) of integers/floats and have the same size
    """
    if not check_matrix(matrix):
        raise TypeError("matrix must be a matrix\
 (list of lists) of integers/floats")
    if not check_matrix_size(matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not check_value(div):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    else:
        return [[round(x/div, 2) for x in j] for j in matrix]


def check_matrix(matrix):
    if not isinstance(matrix, list):
        return False
    for i in matrix:
        if type(i) is not list:
            return False
        if any(not isinstance(y, (int, float)) for y in i):
            return False
    return True


def check_matrix_size(matrix):
    for i in matrix:
        if len(i) == len(matrix[0]):
            pass
        else:
            return False
    return True


def check_value(x):
    """check if the number is integer or float"""
    if not isinstance(x, int) and not isinstance(x, float):
        return False
    else:
        return True
