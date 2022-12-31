#!/usr/bin/env python

from typing import Any, TextIO

from aoc.aoc_solver_strategy import solve_problem


def solve_problem_function(input_file: TextIO, **_: Any) -> Any:
    score = 0
    for line in input_file:
        line = line.strip()
        (t1, t2) = line.split()

        if t2 == "X":  # Lose
            if t1 == "A":
                score += 3
            elif t1 == "B":
                score += 1
            else:
                score += 2
        elif t2 == "Y":  # Draw
            score += 3
            if t1 == "A":
                score += 1
            elif t1 == "B":
                score += 2
            else:
                score += 3
        else:  # Win
            score += 6
            if t1 == "A":
                score += 2
            elif t1 == "B":
                score += 3
            else:
                score += 1

    return score


solve_problem(__file__, solve_problem_function)
