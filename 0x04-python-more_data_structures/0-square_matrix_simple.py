#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_mtrx = matrix.copy()

    for i in range(len(matrix)):
        new_mtrx[i] = list(map(lambda x: x**2, matrix[i]))

    return (new_mtrx)
