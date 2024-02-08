#!/usr/bin/python3
"""This module define the island_perimeter function
"""


def island_perimeter(grid):
    """Calculatesthe perimeter of the island in grid
    """
    grid_sides = {}
    rows = len(grid)
    cols = len(grid[0])

    for row in range(rows):
        for col in range(cols):
            is_land = grid[row][col]
            if is_land:
                for j, i in (
                  (row-1, col), (row+1, col),
                  (row, col-1), (row, col+1)):
                    key = f"{j}-{i}"
                    if key in grid_sides:
                        grid_sides[key] += 1
                    else:
                        grid_sides[key] = 1

    return sum((num for num in grid_sides.values() if num == 1))
