#!/usr/bin/python3


def pascal_triangle(n):
    """Return a an array of arrays containing Pascal's triangle
    """
    if n <= 0:
        return []

    # create list triangle
    triangle = [[1 for i in range(j + 1)] for j in range(n)]

    for row_n, row in enumerate(triangle):
        for col in range(len(row) - 1):
            if col is 0:  # skip [n][0] index
                continue
            triangle[row_n][col] = triangle[row_n - 1][col - 1] + triangle[row_n - 1][col]
    return triangle
