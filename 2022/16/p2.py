#!/usr/bin/env python

from typing import Any, Deque, Dict, List, Optional, Set, TextIO, Tuple

from collections import deque
from itertools import combinations, permutations
import re

from aoc.aoc_solver_strategy import solve_problem


def compute_distances_to_other_nodes(
    all_connecting_nodes: Dict[str, List[str]], source_node: str, dest_nodes: List[str]
) -> Dict[str, int]:
    nodes_to_check: Deque[Tuple[str, int]] = deque()
    nodes_to_check.append((source_node, 0))
    visited_nodes: Set[str] = set()
    distances_to_dest_nodes: Dict[str, int] = {}
    while 0 != len(nodes_to_check):
        curr_node, distance_to_curr_node = nodes_to_check.popleft()
        for connecting_node in all_connecting_nodes[curr_node]:
            if connecting_node in visited_nodes:
                continue
            visited_nodes.add(connecting_node)

            if connecting_node in dest_nodes:
                distances_to_dest_nodes[connecting_node] = distance_to_curr_node + 1

            nodes_to_check.append((connecting_node, distance_to_curr_node + 1))

    return distances_to_dest_nodes


def compute_max_pressure_released(
    valve_flow_rates: Dict[str, int],
    start_distances: Dict[str, int],
    distances_between_valves: Dict[str, Dict[str, int]],
) -> int:
    num_workers = 2
    starting_minutes_remaining = 26

    states_to_check: List[
        Tuple[List[Tuple[str, int]], Set[str], int]
    ] = (
        []
    )  # Tuples of List of valve position and minutes remaining pairs, valves unopened, and pressure released
    for combination in combinations(start_distances.keys(), num_workers):
        worker_states: List[Tuple[str, int]] = []
        pressure_released = 0
        for node_name in combination:
            new_minutes_remaining = (
                starting_minutes_remaining - start_distances[node_name] - 1
            )
            if new_minutes_remaining <= 0:
                break
            worker_states.append((node_name, new_minutes_remaining))
            pressure_released += valve_flow_rates[node_name] * new_minutes_remaining

        if num_workers != len(worker_states):
            continue

        states_to_check.append(
            (
                worker_states,
                set(valve_flow_rates.keys()) - set(combination),
                pressure_released,
            )
        )
    # print(f"states_to_check={states_to_check}")

    max_pressure_released = 0
    while 0 != len(states_to_check):
        (
            worker_states,
            valves_unopened,
            pressure_released,
        ) = states_to_check.pop()

        added_to_states_to_check = False
        for permutation in permutations(valves_unopened, len(worker_states)):
            new_worker_states: List[Tuple[str, int]] = []
            new_valves_unopened = valves_unopened.copy()
            new_pressure_released = pressure_released
            for (curr_node_name, minutes_remaining), node_name in zip(
                worker_states, permutation
            ):
                distance = distances_between_valves[curr_node_name][node_name]
                new_minutes_remaining = minutes_remaining - distance - 1
                if new_minutes_remaining <= 0:
                    continue

                new_valves_unopened.remove(node_name)
                new_pressure_released += (
                    valve_flow_rates[node_name] * new_minutes_remaining
                )
                new_worker_states.append((node_name, new_minutes_remaining))

            if 0 != len(new_worker_states):
                added_to_states_to_check = True
                states_to_check.append(
                    (
                        new_worker_states,
                        new_valves_unopened,
                        new_pressure_released,
                    )
                )

        if not added_to_states_to_check:
            max_pressure_released = max(max_pressure_released, pressure_released)

    return max_pressure_released


def solve_problem_function(input_file: TextIO, **_: Any) -> Any:
    start_node_name = "AA"

    all_connecting_nodes: Dict[str, List[str]] = {}
    valve_flow_rates: Dict[
        str, int
    ] = {}  # tuples of flow rate and distances to other valves
    for line in input_file:
        line = line.strip()
        if 0 == len(line):
            continue
        # print(f"line={line}")
        m = re.search(
            "Valve (\w+) has flow rate=(\d+); tunnel[s]* lead[s]* to valve[s]* (.+)",
            line,
        )
        if m is None:
            continue
        node_name = m.group(1)
        valve_flow_rate = int(m.group(2))
        connecting_node_names = [x.strip() for x in m.group(3).split(",")]
        all_connecting_nodes[node_name] = connecting_node_names
        if valve_flow_rate > 0:
            valve_flow_rates[node_name] = valve_flow_rate
    # print(f"all_connecting_nodes={all_connecting_nodes}")
    # print(f"valve_flow_rates={valve_flow_rates}")

    start_distances = compute_distances_to_other_nodes(
        all_connecting_nodes, start_node_name, list(valve_flow_rates.keys())
    )
    # print(f"start_distances={start_distances}")
    distances_between_valves: Dict[str, Dict[str, int]] = {}
    for node_name in valve_flow_rates:
        distances_between_valves[node_name] = compute_distances_to_other_nodes(
            all_connecting_nodes, node_name, list(valve_flow_rates.keys())
        )
    # print(f"distances_between_valves={distances_between_valves}")

    return compute_max_pressure_released(
        valve_flow_rates, start_distances, distances_between_valves
    )


solve_problem(__file__, solve_problem_function)
