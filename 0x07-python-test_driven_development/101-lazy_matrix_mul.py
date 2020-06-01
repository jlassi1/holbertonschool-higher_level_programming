#!/usr/bin/python3
import numpy
"""
Matrix multiplication  by using the module NumPy
"""


def lazy_matrix_mul(m_a, m_b):
    """function that multiplies 2 matrices by using the module NumPy"""
    m1 = numpy.array(m_a)
    m2 = numpy.array(m_b)
    m_R = numpy.dot(m1, m2)
    return m_R
