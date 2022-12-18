#!/usr/bin/env python

from typing import TextIO

from aoc.aoc_solver_strategy import solve_problem


def get_value(char: str) -> int:
    if char.isupper():
        return ord(char) - ord('A') + 27
    return ord(char) - ord('a') + 1


def solve_problem_function(input_file: TextIO) -> str:
    sum = 0
    sets = []
    for line in input_file:
        sets.append(set(line.strip()))

        if len(sets) == 3:
            intersection = sets[0].intersection(sets[1]).intersection(sets[2])
            if 1 == len(intersection):
                item = intersection.pop()

                sum += get_value(item)
            else:
                print(f"s1={sets[0]}; s2={sets[1]}; s3={sets[2]}")
            sets = []

    return str(sum)


solve_problem(__file__, solve_problem_function)
