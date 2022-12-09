# Day 09: Rope Bridge
from pathlib import Path

from typing import List, Set, Tuple


class Bridge:
    knots = List[Tuple[int, int]]
    tail_position_history: Set[Tuple[int, int]]

    def __init__(self, num_knots: int = 2):
        self.knots = [(0, 0) for _ in range(num_knots)]
        self.tail_position_history = {(0, 0)}

    def _move_head(self, direction: str, magnitude: int):
        dx, dy = 0, 0
        if direction == "L":
            dx = -1
        elif direction == "R":
            dx = 1
        elif direction == "D":
            dy = -1
        else:
            dy = 1

        for _ in range(magnitude):
            head_x, head_y = self.knots[0]
            self.knots[0] = (head_x + dx, head_y + dy)

            tail_dx = dx
            tail_dy = dy
            for knot_idx in range(1, len(self.knots)):
                last_x, last_y = self.knots[knot_idx - 1]
                my_x, my_y = self.knots[knot_idx]

                if abs(my_x - last_x) > 1:
                    my_x += tail_dx
                    if my_y < last_y:
                        my_y += 1
                        tail_dy = 1
                    elif my_y > last_y:
                        my_y -= 1
                        tail_dy = -1
                    else:
                        tail_dy = 0
                elif abs(my_y - last_y) > 1:
                    my_y += tail_dy
                    if my_x < last_x:
                        my_x += 1
                        tail_dx = 1
                    elif my_x > last_x:
                        my_x -= 1
                        tail_dx = -1
                    else:
                        tail_dx = 0

                self.knots[knot_idx] = (my_x, my_y)
                if knot_idx == len(self.knots) - 1:
                    self.tail_position_history.add((my_x, my_y))
        return

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
    b = Bridge(num_knots=10)
    b.run_motions(lines)
    return len(b.tail_position_history)


if __name__ == "__main__":
    input_path = Path(__file__).parent.joinpath("input.txt")
    with input_path.open() as input_file:
        input_lines = input_file.readlines()
        print(f"Part 1:\t{part1(input_lines)}")
        print(f"Part 2:\t{part2(input_lines)}")
