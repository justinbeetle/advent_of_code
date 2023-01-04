#!/usr/bin/env python

from typing import Any, TextIO

from aoc.aoc_solver_strategy import solve_problem
from aoc.point import Point


def solve_problem_function(input_file: TextIO, **_: Any) -> Any:
    sand_src = Point(500, 0)

    rocks = set()
    lowest_rock_y = sand_src.y  # Down is POSITIVE here!!!
    for line in input_file:
        line.strip()
        prev_point = None
        for point_str in line.split("->"):
            point_str.strip()
            point_coords = point_str.split(",")
            curr_point = Point(int(point_coords[0]), int(point_coords[1]))

            if prev_point is not None:
                prev_to_curr_vec = curr_point - prev_point
                prev_to_curr_mag = int(prev_to_curr_vec.mag())
                prev_to_curr_unit_vec = prev_to_curr_vec // prev_to_curr_mag

                for i in range(prev_to_curr_mag + 1):
                    rock = prev_point + i * prev_to_curr_unit_vec
                    # print(f"Adding rock={rock}")
                    rocks.add(rock)
                    lowest_rock_y = max(lowest_rock_y, rock.y)

            prev_point = curr_point

    # Simulate falling
    sand = set()
    while sand_src not in sand:
        prev_sand_pos = None
        curr_sand_pos = Point(sand_src)
        while curr_sand_pos != prev_sand_pos and curr_sand_pos.y < lowest_rock_y + 1:
            prev_sand_pos = curr_sand_pos
            for falling_direction in [Point(0, 1), Point(-1, 1), Point(1, 1)]:
                new_sand_pos = curr_sand_pos + falling_direction
                if new_sand_pos not in rocks and new_sand_pos not in sand:
                    curr_sand_pos = new_sand_pos
                    break

        # print(f"Adding sand={curr_sand_pos}")
        sand.add(curr_sand_pos)
    # print(f"sand={sand}")

    return len(sand)


solve_problem(__file__, solve_problem_function)
