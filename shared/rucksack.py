import string
from pathlib import Path

from typing import List


def item_priority(item: string) -> int:
    return string.ascii_letters.index(item) + 1


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


def parse(rucksack_path: Path) -> List[Rucksack]:
    rucksacks = []

    with rucksack_path.open() as rucksack_file:
        for line in rucksack_file.readlines():
            line = line.strip()
            if len(line) > 0:
                rucksacks.append(Rucksack(line))

    return rucksacks
