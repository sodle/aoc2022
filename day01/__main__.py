# Day 01: Calorie Counting
from pathlib import Path

from typing import List

from shared import parse_elves


def part1(elves: List[List[int]]) -> int:
    # A list of elves, each represented by the list of fruits they carry, each represented as a calorie count
    max_cals = 0
    for elf_calories in elves:
        cals = sum(elf_calories)
        if cals > max_cals:
            max_cals = cals
    return max_cals


def part2(elves: List[List[int]]) -> int:
    elf_sums = [sum(elf) for elf in elves]
    sorted_elf_sums = sorted(elf_sums, reverse=True)
    return sum(sorted_elf_sums[:3])


def main():
    input_path = Path(__file__).parent.joinpath("input.txt")
    elves = parse_elves(input_path)
    print(f"Part 1:\t{part1(elves)}")
    print(f"Part 2:\t{part2(elves)}")


if __name__ == "__main__":
    main()
