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


def parse(patrols_path: Path) -> List[Patrol]:
    patrols = []

    with patrols_path.open() as patrols_file:
        for line in patrols_file:
            line = line.strip()
            patrols.append(Patrol(line))

    return patrols
