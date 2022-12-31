#!/usr/bin/env python

from typing import Any, TextIO

from aoc.aoc_solver_strategy import solve_problem
from aoc.point import Point


def solve_problem_function(input_file: TextIO, **_: Any) -> Any:
    head_position = Point(0, 0)
    tail_position = Point(0, 0)
    tail_positions = set()
    tail_positions.add(tail_position)
    for line in input_file:
        line = line.strip()
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
            new_head_position = head_position + dir_vec
            if (new_head_position - tail_position).mag() >= 2:
                tail_position = head_position
                tail_positions.add(tail_position)

            head_position = new_head_position

    return len(tail_positions)


solve_problem(__file__, solve_problem_function)
