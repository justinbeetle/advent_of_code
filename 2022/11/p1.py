#!/usr/bin/env python

from __future__ import annotations
from typing import Dict, List, TextIO

from aoc.aoc_solver_strategy import solve_problem


class Monkey:
    def __init__(self, num: int):
        self.num = num
        self.items: List[int] = []
        self.operation = ""
        self.test_div_by = 0
        self.test_true_next_monkey = 0
        self.test_false_next_monkey = 0
        self.items_inspected = 0

    def take_turn(self, monkeys: Dict[Monkey]) -> None:
        for (
            old
        ) in (
            self.items
        ):  # The name old is special as it is used in the operation string
            new = eval(self.operation) // 3
            if 0 == new % self.test_div_by:
                next_monkey = self.test_true_next_monkey
            else:
                next_monkey = self.test_false_next_monkey
            monkeys[next_monkey].items.append(new)
            self.items_inspected += 1
        self.items.clear()


def solve_problem_function(input_file: TextIO) -> str:
    monkeys: Dict[Monkey] = {}

    for line in input_file:
        line = line.strip()
        if line.startswith("Monkey"):
            monkey = Monkey(int(line.split()[-1][:-1]))
            monkeys[monkey.num] = monkey
        elif line.startswith("Starting items:"):
            monkey.items = [int(x) for x in line.split(":")[-1].split(",")]
        elif line.startswith("Operation:"):
            monkey.operation = line.split("=")[-1]
        elif line.startswith("Test:"):
            monkey.test_div_by = int(line.split()[-1])
        elif line.startswith("If true:"):
            monkey.test_true_next_monkey = int(line.split()[-1])
        elif line.startswith("If false:"):
            monkey.test_false_next_monkey = int(line.split()[-1])

    for _ in range(20):
        # print(f"_={_}")
        for key in monkeys:
            monkeys[key].take_turn(monkeys)
            # print(f"key={key}; monkeys[key]={monkeys[key].__dict__}")

    highest = sorted([x.items_inspected for x in monkeys.values()])[-2:]
    return str(highest[0] * highest[1])


solve_problem(__file__, solve_problem_function)
