# Day 14: Regolith Reservoir
import functools
from pathlib import Path
import json

from typing import Union, Optional


def part1(lines: list[str]) -> int:
    rock_coordinates = []
    deepest_row = 0

    for line in lines:
        line = line.strip()
        if len(line) == 0:
            continue

        points = line.split(" -> ")
        for idx, point in enumerate(points):
            if idx < len(points) - 1:
                from_x, from_y = point.split(",")
                to_x, to_y = points[idx+1].split(",")

                if from_x > to_x:
                    swap = from_x
                    from_x = to_x
                    to_x = swap

                if from_y > to_y:
                    swap = from_y
                    from_y = to_y
                    to_y = swap

                for x in range(int(from_x), int(to_x) + 1):
                    for y in range(int(from_y), int(to_y) + 1):
                        rock_coordinates.append((x, y))
                        if y > deepest_row:
                            deepest_row = y

    rested_grains = 0
    while True:
        grain_x = 500
        grain_y = 0
        while True:
            if (grain_x, grain_y + 1) not in rock_coordinates:
                grain_y += 1
            elif (grain_x - 1, grain_y + 1) not in rock_coordinates:
                grain_x -= 1
                grain_y += 1
            elif (grain_x + 1, grain_y + 1) not in rock_coordinates:
                grain_x += 1
                grain_y += 1
            else:
                rock_coordinates.append((grain_x, grain_y))
                rested_grains += 1
                break

            if grain_y >= deepest_row:
                return rested_grains


def part2(lines: list[str]) -> int:
    rock_coordinates = []
    deepest_row = 0

    for line in lines:
        line = line.strip()
        if len(line) == 0:
            continue

        points = line.split(" -> ")
        for idx, point in enumerate(points):
            if idx < len(points) - 1:
                from_x, from_y = point.split(",")
                to_x, to_y = points[idx+1].split(",")

                if from_x > to_x:
                    swap = from_x
                    from_x = to_x
                    to_x = swap

                if from_y > to_y:
                    swap = from_y
                    from_y = to_y
                    to_y = swap

                for x in range(int(from_x), int(to_x) + 1):
                    for y in range(int(from_y), int(to_y) + 1):
                        rock_coordinates.append((x, y))
                        if y > deepest_row:
                            deepest_row = y

    print(deepest_row + 2)

    rested_grains = 0
    while True:
        grain_x = 500
        grain_y = 0
        while True:
            if (grain_x, grain_y + 1) not in rock_coordinates and grain_y < deepest_row + 1:
                grain_y += 1
            elif (grain_x - 1, grain_y + 1) not in rock_coordinates and grain_y < deepest_row + 1:
                grain_x -= 1
                grain_y += 1
            elif (grain_x + 1, grain_y + 1) not in rock_coordinates and grain_y < deepest_row + 1:
                grain_x += 1
                grain_y += 1
            else:
                rock_coordinates.append((grain_x, grain_y))
                rested_grains += 1

                if grain_x == 500 and grain_y == 0:
                    return rested_grains

                break


if __name__ == "__main__":
    input_path = Path(__file__).parent.joinpath("input.txt")
    with input_path.open() as input_file:
        input_lines = input_file.readlines()
        print(f"Part 1:\t{part1(input_lines)}")
        print(f"Part 2:\t{part2(input_lines)}")
