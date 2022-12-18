#!/usr/bin/env python

from typing import TextIO

from aoc.aoc_solver_strategy import solve_problem


def solve_problem_function(input_file: TextIO) -> str:
    counts = []
    curr = 0
    for line in input_file:
        line = line.strip()
        if line == "":
            counts.append(curr)
            curr = 0
        else:
            curr += int(line)

    counts.append(curr)

    counts.sort()

    return str(sum(counts[-3:]))


solve_problem(__file__, solve_problem_function)
