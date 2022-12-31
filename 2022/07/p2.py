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

    file_sys_size = 70000000
    free_space = file_sys_size - dirs[root_path]
    needed_space = 30000000
    min_delete_space = max(0, needed_space - free_space)
    delete_dir_size = file_sys_size
    for dir in dirs:
        if dirs[dir] >= min_delete_space:
            delete_dir_size = min(delete_dir_size, dirs[dir])

    return delete_dir_size


solve_problem(__file__, solve_problem_function)
