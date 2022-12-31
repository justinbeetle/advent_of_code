#!/usr/bin/env python

from typing import Any, TextIO

import ast
import math

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


class Packet:
    def __init__(self, value):
        self.value = value

    def __lt__(self, other):
        if packets_in_order(self.value, other.value):
            return True
        return False

    def __eq__(self, other):
        return self.value == other.value


def solve_problem_function(input_file: TextIO, **_: Any) -> Any:
    div_packets = [Packet([[2]]), Packet([[6]])]
    packets = div_packets[:]
    for line in input_file:
        line = line.strip()
        if 0 == len(line):
            continue
        packets.append(Packet(ast.literal_eval(line)))

    packets.sort()
    div_packet_indexes = []
    for div_packet in div_packets:
        div_packet_indexes.append(packets.index(div_packet) + 1)
    return math.prod(div_packet_indexes)


solve_problem(__file__, solve_problem_function)
