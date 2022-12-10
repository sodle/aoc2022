# Day 10: Cathode-Ray Tube
from pathlib import Path

from typing import List, Callable


def run_program(lines: List[str], on_tick: Callable[[int, int], None]):
    register = 1
    program_counter = 1

    adding = False
    addend = 0

    lines = [line.strip() for line in lines if len(line.strip()) > 0]

    while len(lines) > 0 or adding:
        on_tick(register, program_counter)

        if adding:
            register += addend
            adding = False
        else:
            line = lines.pop(0)
            if line.startswith("addx"):
                _, addend_str = line.split()
                adding = True
                addend = int(addend_str)

        program_counter += 1


def part1(lines: List[str]) -> int:
    interesting_signals: List[int] = []

    def on_tick(register: int, program_counter: int):
        nonlocal interesting_signals

        if program_counter in (20, 60, 100, 140, 180, 220):
            interesting_signals.append(program_counter * register)

    run_program(lines, on_tick)

    return sum(interesting_signals)


def part2(lines: List[str]) -> str:
    raster: str = ""

    def on_tick(register: int, program_counter: int):
        nonlocal raster

        column = (program_counter - 1) % 40
        if column in range(register - 1, register + 2):
            raster += "#"
        else:
            raster += "."
        if column == 39:
            raster += "\n"

    run_program(lines, on_tick)

    return raster


if __name__ == "__main__":
    input_path = Path(__file__).parent.joinpath("input.txt")
    with input_path.open() as input_file:
        input_lines = input_file.readlines()
        print(f"Part 1:\t{part1(input_lines)}")

        input_lines = input_file.readlines()
        print(f"Part 2:\n{part2(input_lines)}")
