#!/usr/bin/env python

from typing import TextIO

import ast

from aoc.aoc_solver_strategy import solve_problem


def packets_in_order(left, right):
    for idx, left_val in enumerate(left):
        try:
            right_val = right[idx]
            if isinstance(left_val, int) and isinstance(right_val, int):
                if left_val == right_val:
                    continue
                return left_val < right_val
            else:
                sub_result = packets_in_order(
                    left_val if isinstance(left_val, list) else [left_val],
                    right_val if isinstance(right_val, list) else [right_val],
                )
                if sub_result is not None:
                    return sub_result
        except:
            return False  # right ran out of items

    if len(left) < len(right):
        return True  # left ran out of items

    return None


def solve_problem_function(input_file: TextIO) -> str:
    indexes_in_order = []
    pair_idx = 1
    pair = []
    for line in input_file:
        line = line.strip()
        if 0 == len(line):
            continue

        pair.append(ast.literal_eval(line))
        if 2 == len(pair):
            # print(f"compare pair[0]={pair[0]} and pair[1]={pair[1]}")
            if packets_in_order(pair[0], pair[1]):
                indexes_in_order.append(pair_idx)

            pair_idx += 1
            pair = []

    return str(sum(indexes_in_order))


solve_problem(__file__, solve_problem_function)
