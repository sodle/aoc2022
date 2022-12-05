# Day 01: Calorie Counting
from pathlib import Path

from typing import List


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


def parse_elves(elf_path: Path) -> List[List[int]]:
    # Parse each elf's bounty into a list of fruits, and return the full list of elves
    elves = []
    current_elf = []

    with elf_path.open() as elf_file:
        for line in elf_file.readlines():
            line = line.strip()
            if len(line) > 0:
                current_elf.append(int(line))
            else:
                elves.append(current_elf)
                current_elf = []

    if len(current_elf) > 0:
        elves.append(current_elf)

    return elves
