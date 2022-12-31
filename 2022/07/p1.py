#!/usr/bin/env python

from typing import Any, TextIO

import os

from aoc.aoc_solver_strategy import solve_problem


def solve_problem_function(input_file: TextIO, **_: Any) -> Any:
    dirs = {}
    root_path = os.path.normpath("/")
    dirs[root_path] = 0
    path = root_path
    for line in input_file:
        line = line.strip()
        if line.startswith("$"):
            tokens = line[1:].strip().split(" ")
            if "cd" == tokens[0]:
                if tokens[1].startswith("/"):
                    path = tokens[1]
                else:
                    path = os.path.join(path, tokens[1])
                path = os.path.normpath(path)
        else:
            tokens = line.split(" ")
            if "dir" != tokens[0]:
                dirs[root_path] += int(tokens[0])
                if path != root_path:
                    path_segments = path[1:].split(root_path)
                    for _ in range(len(path_segments)):
                        temp_path = root_path + root_path.join(path_segments[: _ + 1])
                        if temp_path not in dirs:
                            dirs[temp_path] = 0
                        dirs[temp_path] += int(tokens[0])

    delete_dirs_size = 0
    for dir in dirs:
        if dirs[dir] <= 100000:
            delete_dirs_size += dirs[dir]

    return delete_dirs_size


solve_problem(__file__, solve_problem_function)
