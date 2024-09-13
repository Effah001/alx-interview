#!/usr/bin/python3
"""Rotate 2D matrix"""


def rotate_2d_matrix(matrix):
    n = len(matrix)
    
    # First, transpose the matrix
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    
    # Then, reverse each row
    for i in range(n):
        matrix[i] = matrix[i][::-1]
