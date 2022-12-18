#!/usr/bin/env python

from typing import TextIO

from aoc.aoc_solver_strategy import solve_problem


def get_value(char: str) -> int:
    if char.isupper():
        return ord(char) - ord('A') + 27
    return ord(char) - ord('a') + 1


def solve_problem_function(input_file: TextIO) -> str:
    sum = 0
    for line in input_file:
        line = line.strip()
        s1 = set(line[:len(line)//2])
        s2 = set(line[len(line)//2:])

        intersection = s1.intersection(s2)
        if 1 == len(intersection):
            item = intersection.pop()

            sum += get_value(item)
        else:
            print(f"line={line}; f={line[:len(line)//2]}; b={line[len(line)//2:]} s1={s1}; s2={s2}")

    return str(sum)


solve_problem(__file__, solve_problem_function)
