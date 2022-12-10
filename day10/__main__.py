# Day 10: Cathode-Ray Tube
from pathlib import Path

from typing import List, Set, Tuple


def part1(lines: List[str]) -> int:
    register = 1
    program_counter = 1

    adding = False
    addend = 0

    interesting_signals: List[int] = []

    while True:
        if program_counter in (20, 60, 100, 140, 180, 220):
            interesting_signals.append(program_counter * register)

        if adding:
            register += addend
            adding = False
        elif len(lines) > 0:
            line = lines.pop(0).strip()
            if line.startswith("addx"):
                _, addend_str = line.split()
                adding = True
                addend = int(addend_str)
            elif line == "noop":
                pass
            else:
                break
        else:
            break

        program_counter += 1

    return sum(interesting_signals)


def part2(lines: List[str]) -> str:
    register = 1
    program_counter = 1

    adding = False
    addend = 0

    raster = ""

    while True:
        column = (program_counter - 1) % 40
        if column in range(register - 1, register + 2):
            raster += "#"
        else:
            raster += "."
        if column == 39:
            raster += "\n"
        if program_counter >= 240:
            break

        if adding:
            register += addend
            adding = False
        elif len(lines) > 0:
            line = lines.pop(0).strip()
            if line.startswith("addx"):
                _, addend_str = line.split()
                adding = True
                addend = int(addend_str)
            elif line == "noop":
                pass
            else:
                break
        else:
            break

        program_counter += 1

    return raster


if __name__ == "__main__":
    input_path = Path(__file__).parent.joinpath("input.txt")
    with input_path.open() as input_file:
        input_lines = input_file.readlines()
        print(f"Part 1:\t{part1(input_lines)}")
    with input_path.open() as input_file:
        input_lines = input_file.readlines()
        print(f"Part 2:\n{part2(input_lines)}")
