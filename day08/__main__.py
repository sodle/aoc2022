# Day 08: Treetop Tree House
from pathlib import Path

from typing import List, Set, Tuple


class Forest:
    grid: List[List[int]]

    def __init__(self, lines: List[str]):
        self.grid = []
        for line in lines:
            line = line.strip()
            if len(line) > 0:
                self.grid.append([int(col) for col in line])

    def _visible_left(self) -> Set[Tuple[int, int]]:
        v = set()
        for y in range(len(self.grid)):
            tallest = -1
            for x in range(len(self.grid[y])):
                if self.grid[y][x] > tallest:
                    v.add((x, y))
                    tallest = self.grid[y][x]
        return v

    def _visible_right(self) -> Set[Tuple[int, int]]:
        v = set()
        for y in range(len(self.grid)):
            tallest = -1
            for x in range(len(self.grid[y]))[::-1]:
                if self.grid[y][x] > tallest:
                    v.add((x, y))
                    tallest = self.grid[y][x]
        return v

    def _visible_top(self) -> Set[Tuple[int, int]]:
        v = set()
        for x in range(len(self.grid[0])):
            tallest = -1
            for y in range(len(self.grid)):
                if self.grid[y][x] > tallest:
                    v.add((x, y))
                    tallest = self.grid[y][x]
        return v

    def _visible_bottom(self) -> Set[Tuple[int, int]]:
        v = set()
        for x in range(len(self.grid[0])):
            tallest = -1
            for y in range(len(self.grid))[::-1]:
                if self.grid[y][x] > tallest:
                    v.add((x, y))
                    tallest = self.grid[y][x]
        return v

    def visible_trees(self) -> Set[Tuple[int, int]]:
        return self._visible_top()\
            .union(self._visible_bottom())\
            .union(self._visible_left())\
            .union(self._visible_right())

    def _score_right(self, vx: int, vy: int, vh: int) -> int:
        count = 0
        for x in range(vx+1, len(self.grid[vy])):
            count += 1
            if self.grid[vy][x] >= vh:
                break
        return count

    def _score_left(self, vx: int, vy: int, vh: int) -> int:
        count = 0
        for x in range(vx)[::-1]:
            count += 1
            if self.grid[vy][x] >= vh:
                break
        return count

    def _score_down(self, vx: int, vy: int, vh: int) -> int:
        count = 0
        for y in range(vy+1, len(self.grid)):
            count += 1
            if self.grid[y][vx] >= vh:
                break
        return count

    def _score_up(self, vx: int, vy: int, vh: int) -> int:
        count = 0
        for y in range(vy)[::-1]:
            count += 1
            if self.grid[y][vx] >= vh:
                break
        return count

    def _viewpoint_score(self, vx, vy) -> int:
        vh = self.grid[vy][vx]
        left = self._score_left(vx, vy, vh)
        right = self._score_right(vx, vy, vh)
        down = self._score_down(vx, vy, vh)
        up = self._score_up(vx, vy, vh)
        return right * left * down * up

    def best_viewpoint_score(self) -> int:
        best = 0
        for vy in range(len(self.grid)):
            for vx in range(len(self.grid[vy])):
                score = self._viewpoint_score(vx, vy)
                if score > best:
                    best = score
        return best


def part1(lines: List[str]) -> int:
    f = Forest(lines)
    return len(f.visible_trees())


def part2(lines: List[str]) -> int:
    f = Forest(lines)
    return f.best_viewpoint_score()


if __name__ == "__main__":
    input_path = Path(__file__).parent.joinpath("input.txt")
    with input_path.open() as input_file:
        input_lines = input_file.readlines()
        print(f"Part 1:\t{part1(input_lines)}")
        print(f"Part 2:\t{part2(input_lines)}")
