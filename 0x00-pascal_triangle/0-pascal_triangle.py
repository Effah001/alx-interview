#!/usr/bin/python3
"""
Pascal Triangle
"""


def pascal_triangle(n):

    """
    Generate Pascal's Triangle with n rows.

    Parameters:
    n (int): Number of rows in Pascal's Triangle

    Returns:
    list of lists: Pascal's Triangle up to n rows, or an empty list if n <= 0
    """

    if n <= 0:
        return []

    # Initialize the triangle
    triangle = []

    # Generate each row
    for i in range(n):
        # Start the new row with [1]
        row = [1]

        # Calculate the middle elements using the previous row
        if i > 0:
            for j in range(1, i):
                row.append(triangle[i-1][j-1] + triangle[i-1][j])

        # End the row with [1] if it's not the first row
        if i > 0:
            row.append(1)

        # Append the new row to the triangle
        triangle.append(row)

    return triangle
