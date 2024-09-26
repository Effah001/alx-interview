#!/usr/bin/python3
"""
a function def island_perimeter(grid):
that returns the perimeter of the island described in grid:
"""


def island_perimeter(grid):
    perimeter = 0
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if (nr < 0 or nr >= rows or nc < 0 or
                        nc >= cols or
                        grid[nr][nc] == 0):
                        perimeter += 1

    return perimeter
