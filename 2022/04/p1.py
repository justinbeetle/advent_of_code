#!/usr/bin/env python

from typing import TextIO

from aoc.aoc_solver_strategy import solve_problem


def solve_problem_function(input_file: TextIO) -> str:
    count = 0
    for line in input_file:
        line = line.strip()
        (r1, r2) = line.split(",")
        (r1l, r1u) = r1.split("-")
        (r2l, r2u) = r2.split("-")
        r1l = int(r1l)
        r1u = int(r1u)
        r2l = int(r2l)
        r2u = int(r2u)

        if r1l <= r2l and r1u >= r2u:
            count += 1
        elif r2l <= r1l and r2u >= r1u:
            count += 1

    return str(count)


solve_problem(__file__, solve_problem_function)
