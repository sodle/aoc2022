# Day 03: Rucksack Reorganization
from pathlib import Path

from typing import List

from shared.rucksack import parse, Rucksack, item_priority


def part1(rucksacks: List[Rucksack]) -> int:
    return sum([item_priority(rucksack.first_common_item()) for rucksack in rucksacks])


def part2(rucksacks: List[Rucksack]) -> int:
    priority_sum = 0

    for i in range(0, len(rucksacks), 3):
        for item in rucksacks[i].items:
            if item in rucksacks[i+1].items:
                if item in rucksacks[i+2].items:
                    priority_sum += item_priority(item)
                    break

    return priority_sum


def main():
    input_path = Path(__file__).parent.joinpath("input.txt")
    rucksacks = parse(input_path)
    print(f"Part 1:\t{part1(rucksacks)}")
    print(f"Part 2:\t{part2(rucksacks)}")


if __name__ == "__main__":
    main()
