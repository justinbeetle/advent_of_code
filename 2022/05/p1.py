#!/usr/bin/env python

from typing import TextIO

from aoc.aoc_solver_strategy import solve_problem


def solve_problem_function(input_file: TextIO) -> str:
    stacks = []
    for line in input_file:
        if "[" in line:
            cnt = 0
            reduced_line = ""
            while 1 + cnt * 4 < len(line):
                reduced_line += line[1 + cnt * 4]
                cnt += 1
            print(reduced_line)

            for idx, char in enumerate(reduced_line):
                if char == " ":
                    continue
                while idx + 1 > len(stacks):
                    stacks.append([])
                stacks[idx] += [char]
            print(f"stacks={stacks}")

        elif line.startswith("move "):
            line = line.strip()
            tokens = line.split(" ")
            num = int(tokens[1])
            src = int(tokens[3]) - 1
            dest = int(tokens[5]) - 1
            for _ in range(num):
                stacks[dest] = [stacks[src][0]] + stacks[dest]
                stacks[src] = stacks[src][1:]
            print(f"after line={line}; stacks={stacks}")

    top_elements = ""
    for stack in stacks:
        top_elements += stack[0]
    return top_elements


solve_problem(__file__, solve_problem_function)
