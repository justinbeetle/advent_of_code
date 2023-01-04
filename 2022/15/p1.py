#!/usr/bin/env python

from typing import Any, TextIO

import re

from aoc.aoc_solver_strategy import solve_problem
from aoc.point import Point


def solve_problem_function(input_file: TextIO, **kwargs: Any) -> Any:
    y = 10 if kwargs["is_example"] else 2000000

    sensors = []
    beacon_x_coords_at_y = set()
    for line in input_file:
        line.strip()
        m = re.search(
            "Sensor at x=(-*\d+), y=(-*\d+): closest beacon is at x=(-*\d+), y=(-*\d+)",
            line,
        )
        sensor = Point(int(m.group(1)), int(m.group(2)))
        beacon = Point(int(m.group(3)), int(m.group(4)))
        sensor_range = abs(sensor.x - beacon.x) + abs(sensor.y - beacon.y)
        sensors.append((sensor, sensor_range))
        if y == beacon.y:
            beacon_x_coords_at_y.add(beacon.x)

    no_beacon_x_coords_at_y = set()
    for sensor, sensor_range in sensors:
        y_dist_to_sensor = abs(y - sensor.y)
        if y_dist_to_sensor > sensor_range:
            # print(f"Skipping sensor at {sensor} with range {sensor_range}")
            continue

        x_span = sensor_range - y_dist_to_sensor
        # print(f"x_span={x_span} for sensor at {sensor} with range {sensor_range}")
        for x in range(sensor.x - x_span, sensor.x + x_span + 1):
            if x not in beacon_x_coords_at_y:
                # print(f"   Adding x={x}")
                no_beacon_x_coords_at_y.add(x)

    return len(no_beacon_x_coords_at_y)


solve_problem(__file__, solve_problem_function)
