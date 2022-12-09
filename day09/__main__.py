# Day 09: Rope Bridge
from pathlib import Path

from typing import List, Set, Tuple


class Bridge:
    head_position: Tuple[int, int]
    tail_position: Tuple[int, int]

    tail_position_history: Set[Tuple[int, int]]

    def __init__(self):
        self.head_position = (0, 0)
        self.tail_position = (0, 0)
        self.tail_position_history = {(0, 0)}

    def _move_head(self, direction: str, magnitude: int):
        head_x, head_y = self.head_position
        tail_x, tail_y = self.tail_position
        for _ in range(magnitude):
            if direction in "LR":
                # moving horizontally
                dx = -1 if direction == "L" else 1
                head_x += dx
                if abs(head_x - tail_x) > 1:
                    # need to move the tail as well to catch up
                    tail_x += dx
                    if head_y != tail_y:
                        # if the tail is on a different row, we'll move diagonally instead of horizontally
                        tail_y = head_y
            else:
                # moving vertically
                dy = -1 if direction == "D" else 1
                head_y += dy
                if abs(head_y - tail_y) > 1:
                    # move tail
                    tail_y += dy
                    if head_x != tail_x:
                        tail_x = head_x
            self.tail_position_history.add((tail_x, tail_y))
        self.head_position = (head_x, head_y)
        self.tail_position = (tail_x, tail_y)

    def run_motions(self, motions: List[str]):
        for line in motions:
            direction, magnitude_str = line.split()
            magnitude_int = int(magnitude_str)
            self._move_head(direction, magnitude_int)


def part1(lines: List[str]) -> int:
    b = Bridge()
    b.run_motions(lines)
    return len(b.tail_position_history)


def part2(lines: List[str]) -> int:
    return 0


if __name__ == "__main__":
    input_path = Path(__file__).parent.joinpath("input.txt")
    with input_path.open() as input_file:
        input_lines = input_file.readlines()
        print(f"Part 1:\t{part1(input_lines)}")
        print(f"Part 2:\t{part2(input_lines)}")
