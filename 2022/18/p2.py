#!/usr/bin/env python

from typing import Any, Dict, List, Optional, TextIO, Tuple

from heapq import heappush, heappop

from aoc.aoc_solver_strategy import solve_problem


Point = Tuple[int, int, int]


def get_neighbors(point: Point) -> List[Point]:
    points = []
    (x, y, z) = point
    points.append((x - 1, y, z))
    points.append((x + 1, y, z))
    points.append((x, y - 1, z))
    points.append((x, y + 1, z))
    points.append((x, y, z - 1))
    points.append((x, y, z + 1))
    return points


def a_star(
    coords: List[Point], start: Point, goal: Point, verbose: bool = False
) -> Optional[List[Point]]:
    """Compute a path from start to goal for an NPC using A* search"""

    def h(n: Point) -> float:
        return abs(goal[0] - n[0]) + abs(goal[1] - n[1]) + abs(goal[2] - n[2])

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
        if verbose:
            print(f"\tin a_star; current={current}; open_set={open_set}", flush=True)
        if current == goal:
            break

        for neighbor in get_neighbors(current):
            if verbose:
                print(f"\t\tin a_star; neighbor={neighbor}", flush=True)
            if neighbor in coords:
                if verbose:
                    print(f"\t\t\tin a_star; cannot move to tile", flush=True)
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
        print(f"in a_star; goal is not in came_from={came_from}", flush=True)

    # No path exists
    return None


def solve_problem_function(input_file: TextIO, **kwargs: Any) -> Any:
    coords = []
    for line in input_file:
        line = line.strip()
        (x, y, z) = line.split(",")
        coords.append((int(x), int(y), int(z)))
    # print(f"coord={coords}")

    count = 0
    for point in coords:
        for neighbor in get_neighbors(point):
            # A* is a bad choice here as it looks for the shortest path and adds a lot of unneeded computation, but it
            # was relatively easy for me to throw together as I had an A* implementation lying around.
            if (
                neighbor not in coords
                and a_star(coords, neighbor, (-1, -1, -1)) is not None
            ):
                count += 1

    return str(count)


solve_problem(__file__, solve_problem_function)
