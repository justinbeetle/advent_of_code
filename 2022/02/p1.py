#!/usr/bin/env python

from typing import TextIO

from aoc.aoc_solver_strategy import solve_problem


def solve_problem_function(input_file: TextIO) -> str:
    score = 0
    for line in input_file:
        line = line.strip()
        (t1, t2) = line.split()

        if t2 == "X":
            score += 1
            if t1 == "A":
                score += 3  # Tie
            elif t1 == "C":
                score += 6  # Win
        elif t2 == "Y":
            score += 2
            if t1 == "B":
                score += 3  # Tie
            elif t1 == "A":
                score += 6  # Win
        else:
            score += 3
            if t1 == "C":
                score += 3  # Tie
            elif t1 == "B":
                score += 6  # Win

    return str(score)


solve_problem(__file__, solve_problem_function)
