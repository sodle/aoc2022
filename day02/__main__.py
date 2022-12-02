# Day 02: Rock Paper Scissors
from pathlib import Path

from typing import List

from shared.rps import parse, Match


def part1(matches: List[Match]) -> int:
    return sum([match.score() for match in matches])


def part2(matches: List[Match]) -> int:
    return sum([match.throw() for match in matches])


def main():
    input_path = Path(__file__).parent.joinpath("input.txt")
    matches = parse(input_path)
    print(f"Part 1:\t{part1(matches)}")
    print(f"Part 2:\t{part2(matches)}")


if __name__ == "__main__":
    main()
