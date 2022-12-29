#!/usr/bin/env python

from typing import TextIO

from aoc.aoc_solver_strategy import solve_problem


def solve_problem_function(input_file: TextIO) -> str:
    x = 1
    x_by_cycle = [x]
    for line in input_file:
        line = line.strip()
        # print(f"line={line}")
        if line == "noop":
            x_by_cycle.append(x)
            # print(f"   tick={len(x_by_cycle)-1} ind={len(x_by_cycle)-1} x={x}")
        elif line.startswith("addx "):
            add_value = int(line.split(" ")[1])
            x_by_cycle.append(x)
            # print(f"   tick={len(x_by_cycle)-1} ind={len(x_by_cycle)-1} x={x}")
            x_by_cycle.append(x)
            x += add_value
            # print(f"   tick={len(x_by_cycle)-1} ind={len(x_by_cycle)-1} x={x}")
    x_by_cycle.append(x)
    # print(f"   tick={len(x_by_cycle)-1} ind={len(x_by_cycle)-1} x={x}")
    # print()

    sum = 0
    for idx in range(20, len(x_by_cycle), 40):
        # print(f"tick={idx}; idx={idx}; x_by_cycle[idx]={x_by_cycle[idx]}")
        sum += idx * x_by_cycle[idx]

    return str(sum)


solve_problem(__file__, solve_problem_function)
