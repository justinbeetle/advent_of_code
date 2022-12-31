#!/usr/bin/env python

from typing import TextIO, Dict, List, Optional, Tuple

from heapq import heappush, heappop

from aoc.aoc_solver_strategy import solve_problem
from aoc.point import Point


def get_neighbors(point: Point) -> List[Point]:
    return [point + (-1, 0), point + (1, 0), point + (0, -1), point + (0, 1)]


def a_star(
    grid: List[List[int]], start: Point, goal: Point, verbose: bool = False
) -> Optional[List[Point]]:
    """Compute a path from start to goal for an NPC using A* search"""

    def h(n: Point) -> float:
        return abs(goal[0] - n[0]) + abs(goal[1] - n[1])

    open_set: List[Tuple[float, Point]] = []
    heappush(open_set, (h(start), start))
    came_from: Dict[Point, Point] = {}
    g_score: Dict[Point, float] = {start: 0.0}
    f_score: Dict[Point, float] = {start: h(start)}
    while 0 < len(open_set):
        queued_f_score, current = heappop(open_set)
        if queued_f_score != f_score[current]:
            if verbose:
                print(
                    f"\tin a_star; ignoring current={current}; open_set={open_set}",
                    flush=True,
                )
            continue

        current_val = grid[current.y][current.x]
        if verbose:
            print(
                f"\tin a_star; current={current}; current_val={current_val}; open_set={open_set}",
                flush=True,
            )
        if current == goal:
            break

        for neighbor in get_neighbors(current):
            if neighbor.x < 0 or neighbor.y < 0:
                if verbose:
                    print(f"\t\tin a_star; neighbor={neighbor}", flush=True)
                    print(
                        f"\t\t\tin a_star; neighbor outside grid (negative)", flush=True
                    )
                continue
            try:
                neighbor_val = grid[neighbor.y][neighbor.x]
            except:
                if verbose:
                    print(f"\t\tin a_star; neighbor={neighbor}", flush=True)
                    print(f"\t\t\tin a_star; neighbor outside grid", flush=True)
                continue
            if verbose:
                print(
                    f"\t\tin a_star; neighbor={neighbor}; neighbor_val={neighbor_val}",
                    flush=True,
                )
            if neighbor_val - current_val > 1:
                if verbose:
                    print(f"\t\t\tin a_star; neighbor value too high", flush=True)
                continue
            tentative_g_score = g_score[current] + 1
            if verbose:
                print(
                    f"\t\t\tin a_star; tentative_g_score={tentative_g_score}",
                    flush=True,
                )
            if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                tentative_f_score = tentative_g_score + h(neighbor)
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = tentative_f_score
                heappush(open_set, (tentative_f_score, neighbor))

    if goal in came_from:
        # Reconstruct the path
        reverse_path = []
        while goal != start:
            reverse_path.append(goal)
            goal = came_from[goal]
        return list(reversed(reverse_path))
    elif verbose:
        print(f"in a_star; goal {goal} is not in came_from={came_from}", flush=True)

    # No path exists
    return None


def solve_problem_function(input_file: TextIO) -> str:
    grid = []
    starts = []
    end = Point(0, 0)
    for line in input_file:
        row = []
        line = line.strip()
        for val in line:
            if val in ["a", "S"]:
                starts.append(Point(len(row), len(grid)))
                val = "a"
            elif val == "E":
                end = Point(len(row), len(grid))
                val = "z"
            row.append(ord(val) - ord("a"))
        grid.append(row)

    min_path = -1
    for start in starts:
        path = a_star(grid, start, end)
        if path is None:
            continue
        if min_path < 0:
            min_path = len(path)
        else:
            min_path = min(min_path, len(path))

    return str(min_path)


solve_problem(__file__, solve_problem_function)
