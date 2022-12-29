#!/usr/bin/env python

from typing import TextIO

from aoc.aoc_solver_strategy import solve_problem
from aoc.point import Point


def solve_problem_function(input_file: TextIO) -> str:
    num_elems = 10
    positions = [Point(0, 0)] * num_elems
    tail_positions = set()
    tail_positions.add(positions[0])
    for line in input_file:
        line = line.strip()
        # print(f"line={line}")
        dir, dist = line.split(" ")
        if dir == "U":
            dir_vec = Point(0, 1)
        elif dir == "D":
            dir_vec = Point(0, -1)
        elif dir == "L":
            dir_vec = Point(-1, 0)
        elif dir == "R":
            dir_vec = Point(1, 0)
        dist = int(dist)
        for _ in range(dist):
            positions[0] += dir_vec
            for pos_idx in range(1, num_elems):
                distance = (positions[pos_idx - 1] - positions[pos_idx]).mag()
                if distance < 2:
                    break

                if positions[pos_idx].x == positions[pos_idx - 1].x:
                    if positions[pos_idx].y < positions[pos_idx - 1].y:
                        positions[pos_idx] += (0, 1)
                    else:
                        positions[pos_idx] -= (0, 1)
                elif positions[pos_idx].y == positions[pos_idx - 1].y:
                    if positions[pos_idx].x < positions[pos_idx - 1].x:
                        positions[pos_idx] += (1, 0)
                    else:
                        positions[pos_idx] -= (1, 0)
                else:
                    if positions[pos_idx].x < positions[pos_idx - 1].x:
                        positions[pos_idx] += (1, 0)
                    else:
                        positions[pos_idx] -= (1, 0)

                    if positions[pos_idx].y < positions[pos_idx - 1].y:
                        positions[pos_idx] += (0, 1)
                    else:
                        positions[pos_idx] -= (0, 1)

                if pos_idx == num_elems - 1:
                    tail_positions.add(positions[-1])
                # print(f"      positions={positions}")

            # print(f"   positions={positions}")
        # print(f"positions={positions}")

    return str(len(tail_positions))


solve_problem(__file__, solve_problem_function)

"""
Input:
R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2
Answer: 1

Alternate Input:
R 5
U 8
L 8
D 3
R 17
D 10
L 25
U 20
Alternate answer: 36
"""
