# Day 04: Camp Cleanup
from pathlib import Path

from typing import List


class Patrol:
    start_a: int
    end_a: int

    start_b: int
    end_b: int

    def __init__(self, line: str):
        range_a, range_b = line.split(",")

        start_a, end_a = range_a.split("-")
        self.start_a = int(start_a)
        self.end_a = int(end_a)

        start_b, end_b = range_b.split("-")
        self.start_b = int(start_b)
        self.end_b = int(end_b)

    def has_total_overlap(self) -> bool:
        if self.start_b >= self.start_a and self.end_b <= self.end_a:
            return True
        if self.start_b <= self.start_a and self.end_b >= self.end_a:
            return True
        return False

    def has_any_overlap(self) -> bool:
        a = set(range(self.start_a, self.end_a+1))
        b = set(range(self.start_b, self.end_b+1))
        return not a.isdisjoint(b)


def part1(patrols: List[Patrol]) -> int:
    return len([patrol for patrol in patrols if patrol.has_total_overlap()])


def part2(patrols: List[Patrol]) -> int:
    return len([patrol for patrol in patrols if patrol.has_any_overlap()])


def main():
    input_path = Path(__file__).parent.joinpath("input.txt")
    patrols = parse(input_path)
    print(f"Part 1:\t{part1(patrols)}")
    print(f"Part 2:\t{part2(patrols)}")


if __name__ == "__main__":
    main()


def parse(patrols_path: Path) -> List[Patrol]:
    patrols = []

    with patrols_path.open() as patrols_file:
        for line in patrols_file:
            line = line.strip()
            patrols.append(Patrol(line))

    return patrols
