#!/usr/bin/env python

from typing import TextIO

from aoc.aoc_solver_strategy import solve_problem


def get_neighbors(point):
    points = []
    (x, y, z) = point
    points.append((x - 1, y, z))
    points.append((x + 1, y, z))
    points.append((x, y - 1, z))
    points.append((x, y + 1, z))
    points.append((x, y, z - 1))
    points.append((x, y, z + 1))
    return points


def solve_problem_function(input_file: TextIO) -> str:
    coords = []
    for line in input_file:
        line = line.strip()
        (x, y, z) = line.split(",")
        coords.append((int(x), int(y), int(z)))

    count = 0
    for point in coords:
        for neighbor in get_neighbors(point):
            if neighbor not in coords:
                count += 1

    return str(count)


solve_problem(__file__, solve_problem_function)
