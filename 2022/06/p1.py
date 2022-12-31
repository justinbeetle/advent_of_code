#!/usr/bin/env python

from typing import Any, TextIO

from aoc.aoc_solver_strategy import solve_problem


def solve_problem_function(input_file: TextIO, **_: Any) -> Any:
    NUM_UNIQUE = 4
    for line in input_file:
        line = line.strip()
        for i in range(0, len(line) - NUM_UNIQUE):
            # print(f"i={i}; {line[i:i+NUM_UNIQUE]}")
            if NUM_UNIQUE == len(set(line[i : i + NUM_UNIQUE])):
                return i + NUM_UNIQUE


solve_problem(__file__, solve_problem_function)
