# Day 03: Rucksack Reorganization
import string
from pathlib import Path

from typing import List


class Rucksack:
    compartment_1: string
    compartment_2: string
    items: string

    def __init__(self, items: string):
        half_idx = len(items) // 2
        self.compartment_1 = items[:half_idx]
        self.compartment_2 = items[half_idx:]
        self.items = items

    def first_common_item(self) -> str:
        for item in self.compartment_1:
            if item in self.compartment_2:
                return item


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


def item_priority(item: string) -> int:
    return string.ascii_letters.index(item) + 1


def parse(rucksack_path: Path) -> List[Rucksack]:
    rucksacks = []

    with rucksack_path.open() as rucksack_file:
        for line in rucksack_file.readlines():
            line = line.strip()
            if len(line) > 0:
                rucksacks.append(Rucksack(line))

    return rucksacks


test_data_path = Path(__file__).parent.joinpath("test_data")


def test_item_priority():
    assert item_priority("a") == 1
    assert item_priority("A") == 27


def test_parse_rucksacks():
    rucksacks = parse(test_data_path.joinpath("rucksacks.txt"))
    assert rucksacks[0].first_common_item() == "p"
    assert rucksacks[1].first_common_item() == "L"
    assert rucksacks[2].first_common_item() == "P"
    assert rucksacks[3].first_common_item() == "v"
    assert rucksacks[4].first_common_item() == "t"
    assert rucksacks[5].first_common_item() == "s"
