# Day 04: Camp Cleanup
from pathlib import Path

from typing import List

from shared.patrols import parse, Patrol


def part1(patrols: List[Patrol]) -> int:
    return len([patrol for patrol in patrols if patrol.has_total_overlap()])


def part2(patrols: List[Patrol]) -> int:
    return len([patrol for patrol in patrols if patrol.has_any_overlap()])


def main():
    input_path = Path(__file__).parent.joinpath("input.txt")
    rucksacks = parse(input_path)
    print(f"Part 1:\t{part1(rucksacks)}")
    print(f"Part 2:\t{part2(rucksacks)}")


if __name__ == "__main__":
    main()
