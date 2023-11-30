#!/usr/bin/python3
""" This module defines a pascal triangle
imentation
"""

def pascal_triangle(n):
    """ Implements a pascal triangle

    Arguments:
    =========
    n (integer) - height of pascal triangle

    Returns - List of list representing the triangle
    """
    triangle = [[1]]
    if n == 0:
        return []
    if n == 1:
        return triangle

    prev = triangle[0]
    nex = []

    for row in range(2, n + 1):
        for col in range(row):
            if col == 0:
                nex.append(1)
            elif col == len(prev):
                nex.append(1)
            else:
                top_left = prev[col - 1]
                top_right = prev[col]
                nex.append(top_left + top_right)
        triangle.append(nex)
        prev = nex[:]
        nex = []
    return triangle
