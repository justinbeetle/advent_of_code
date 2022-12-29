#!/usr/bin/env python

from typing import TextIO

from aoc.aoc_solver_strategy import solve_problem


def solve_problem_function(input_file: TextIO) -> str:
    x = 1
    tick = 0
    output = ""

    def get_output():
        new_output = ""
        tick_x_pos = tick % 40
        if tick > 0 and 0 == tick_x_pos:
            new_output += "\n"
        if abs(tick_x_pos - x) <= 1:
            new_output += "#"
        else:
            new_output += "."
        return new_output

    for line in input_file:
        line = line.strip()
        # print(f"line={line}")
        output += get_output()
        tick += 1
        if line.startswith("addx "):
            add_value = int(line.split(" ")[1])
            output += get_output()
            tick += 1
            x += add_value

    return output


solve_problem(__file__, solve_problem_function)
