#!/usr/bin/env python

from typing import TextIO

from aoc.aoc_solver_strategy import solve_problem


def solve_problem_function(input_file: TextIO) -> str:
    max = 0
    curr = 0
    for line in input_file:
        line = line.strip()
        if line == "":
            if curr > max:
                max = curr
            curr = 0
        else:
            curr += int(line)

    if curr > max:
        max = curr

    return str(max)


solve_problem(__file__, solve_problem_function)
