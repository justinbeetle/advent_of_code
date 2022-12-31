#!/usr/bin/env python

from typing import Any, TextIO

from aoc.aoc_solver_strategy import solve_problem


def solve_problem_function(input_file: TextIO, **_: Any) -> Any:
    trees = []
    for line in input_file:
        tree_row = []
        line = line.strip()
        for tree in line:
            tree_row.append(int(tree))
        trees.append(tree_row)

    width = len(trees[0])
    height = len(trees)
    max_score = 0
    for x in range(1, width - 1):
        tree_col = []
        for y in range(height):
            tree_col.append(trees[y][x])

        for y in range(1, height - 1):
            tree = trees[y][x]
            tree_row = trees[y]
            left = 1
            right = 1
            up = 1
            down = 1

            while x - left > 0 and tree > tree_row[x - left]:
                left += 1
            while x + right < width - 1 and tree > tree_row[x + right]:
                right += 1
            while y - up > 0 and tree > tree_col[y - up]:
                up += 1
            while y + down < height - 1 and tree > tree_col[y + down]:
                down += 1

            score = left * right * up * down
            max_score = max(score, max_score)

    return max_score


solve_problem(__file__, solve_problem_function)
