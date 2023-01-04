#!/usr/bin/env python

from typing import Any, TextIO

import numpy
import re
import sys

from aoc.aoc_solver_strategy import solve_problem
from aoc.point import Point


class Range:
    def __init__(self, min: int, max: int) -> None:
        self.sub_ranges = [(min, max)]

    def union(self, other_min: int, other_max: int) -> None:
        add_new_subrange = True
        for idx, (sub_range_min, sub_range_max) in enumerate(self.sub_ranges):
            if other_min > sub_range_max + 1 or other_max + 1 < sub_range_min:
                # The two ranges are distinct
                continue

            # The two ranges overlap
            add_new_subrange = False

            sub_range_min = min(other_min, sub_range_min)
            sub_range_max = max(other_max, sub_range_max)
            self.sub_ranges[idx] = (sub_range_min, sub_range_max)

            # Check for subsequent sub_ranges need to be merged into this sub_range
            next_idx = idx + 1
            while (
                next_idx < len(self.sub_ranges)
                and self.sub_ranges[next_idx][0] <= sub_range_max + 1
            ):
                sub_range_max = max(self.sub_ranges[next_idx][1], sub_range_max)
                self.sub_ranges[idx] = (sub_range_min, sub_range_max)
                self.sub_ranges.pop(next_idx)
            break

        if add_new_subrange:
            for idx, (sub_range_min, sub_range_max) in enumerate(self.sub_ranges):
                if other_min < sub_range_min:
                    self.sub_ranges.insert(idx, (other_min, other_max))
                    add_new_subrange = False
                    break

            if add_new_subrange:
                self.sub_ranges.append((other_min, other_max))

    def __eq__(self, other):
        return self.sub_ranges == other.sub_ranges

    def __str__(self):
        return str(self.sub_ranges)

    def __repr__(self):
        return repr(self.sub_ranges)


def solve_problem_function(input_file: TextIO, **kwargs: Any) -> Any:
    min_coord = 0
    max_coord = 20 if kwargs["is_example"] else 4000000
    full_range = Range(min_coord, max_coord)

    sensors = []
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

    for y in range(max_coord + 1):
        if 0 == y % 250000:
            print(f"Checking y={y}", flush=True)

        no_beacon_range = None
        for sensor, sensor_range in sensors:
            y_dist_to_sensor = abs(y - sensor.y)
            if y_dist_to_sensor > sensor_range:
                # print(f"Skipping sensor at {sensor} with range {sensor_range}")
                continue

            x_span = sensor_range - y_dist_to_sensor
            min_x = max(min_coord, sensor.x - x_span)
            max_x = min(max_coord, sensor.x + x_span)
            if no_beacon_range is None:
                no_beacon_range = Range(min_x, max_x)
            else:
                no_beacon_range.union(min_x, max_x)

            if full_range == no_beacon_range:
                break

        if full_range != no_beacon_range:
            subrange = no_beacon_range.sub_ranges[0]
            if 1 == len(no_beacon_range.sub_ranges):
                if min_coord != subrange[0]:
                    x = min_coord
                else:
                    x = max_coord
            else:
                x = subrange[1] + 1

            return 4000000 * x + y

        """ This worked but was very, very slow
        no_beacon_x_coords_at_y = numpy.ones(max_coord, dtype=numpy.int8)
        for sensor, sensor_range in sensors:
            y_dist_to_sensor = abs(y - sensor.y)
            if y_dist_to_sensor > sensor_range:
                # print(f"Skipping sensor at {sensor} with range {sensor_range}")
                continue

            x_span = sensor_range - y_dist_to_sensor
            min_x = max(min_coord, sensor.x - x_span)
            max_x = min(max_coord, sensor.x + x_span)
            if min_x == min_coord and max_x == max_coord:
                no_beacon_x_coords_at_y = numpy.zeros(1)
                break

            no_beacon_x_coords_at_y[min_x:max_x+1] = 0

        non_zero_x = no_beacon_x_coords_at_y.nonzero()[0]
        if 1 == len(non_zero_x):
            return 4000000 * non_zero_x[0] + y
        """

    sys.exit("FAIL: Failed to find the beacon!!!")


solve_problem(__file__, solve_problem_function)
