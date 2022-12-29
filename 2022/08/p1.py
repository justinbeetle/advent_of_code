#!/usr/bin/env python

from typing import TextIO

from aoc.aoc_solver_strategy import solve_problem


def solve_problem_function(input_file: TextIO) -> str:
    trees = []
    for line in input_file:
        tree_row = []
        line = line.strip()
        for tree in line:
            tree_row.append(int(tree))
        trees.append(tree_row)

    width = len(trees[0])
    height = len(trees)
    count = 2 * width + 2 * height - 4
    for x in range(1, width - 1):
        tree_col = []
        for y in range(height):
            tree_col.append(trees[y][x])

        for y in range(1, height - 1):
            tree = trees[y][x]
            tree_row = trees[y]

            if (
                tree > max(tree_col[0:y])
                or tree > max(tree_col[y + 1 :])
                or tree > max(tree_row[0:x])
                or tree > max(tree_row[x + 1 :])
            ):
                count += 1

    return str(count)


solve_problem(__file__, solve_problem_function)
