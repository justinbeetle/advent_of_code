#!/usr/bin/env python

from typing import TextIO

from aoc.aoc_solver_strategy import solve_problem


def get_value(char: str) -> int:
    if char.isupper():
        return ord(char) - ord("A") + 27
    return ord(char) - ord("a") + 1


def solve_problem_function(input_file: TextIO) -> str:
    NUM_UNIQUE = 4
    for line in input_file:
        line = line.strip()
        for i in range(0, len(line) - NUM_UNIQUE):
            print(f"i={i}; {line[i:i+NUM_UNIQUE]}")
            if NUM_UNIQUE == len(set(line[i : i + NUM_UNIQUE])):
                return str(i + NUM_UNIQUE)


solve_problem(__file__, solve_problem_function)
