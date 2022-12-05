# Day 02: Rock Paper Scissors
from enum import IntEnum
from pathlib import Path

from typing import List


class Shape(IntEnum):
    # map of hand shape -> score
    ROCK = 1
    PAPER = 2
    SCISSORS = 3


class Match:
    my_play: Shape
    their_play: Shape

    def __init__(self, line: str):
        [their_letter, my_letter] = line.split(" ")

        self.their_play = {
            "A": Shape.ROCK,
            "B": Shape.PAPER,
            "C": Shape.SCISSORS
        }[their_letter]

        self.my_play = {
            "X": Shape.ROCK,
            "Y": Shape.PAPER,
            "Z": Shape.SCISSORS
        }[my_letter]

    def score(self) -> int:
        score = self.my_play

        if self.my_play == self.their_play:
            # draw, 3-point bonus
            return score + 3

        if self.my_play == Shape.ROCK:
            if self.their_play == Shape.SCISSORS:
                # rock smashes scissors, 6-point bonus
                return score + 6

        if self.my_play == Shape.PAPER:
            if self.their_play == Shape.ROCK:
                # paper covers rock, 6-point bonus
                return score + 6

        if self.my_play == Shape.SCISSORS:
            if self.their_play == Shape.PAPER:
                # scissors cuts paper, 6-point bonus
                return score + 6

        # loss, no bonus
        return score

    def throw(self) -> int:
        expected_bonus = 3 * (self.my_play - 1)

        if expected_bonus == 0:
            # we need to lose
            if self.their_play == Shape.ROCK:
                return Shape.SCISSORS
            elif self.their_play == Shape.PAPER:
                return Shape.ROCK
            else:
                return Shape.PAPER
        elif expected_bonus == 3:
            # we need to tie
            return self.their_play + 3
        else:
            # we need to win
            if self.their_play == Shape.ROCK:
                return Shape.PAPER + 6
            elif self.their_play == Shape.PAPER:
                return Shape.SCISSORS + 6
            else:
                return Shape.ROCK + 6


def parse(rps_path: Path) -> List[Match]:
    matches = []

    with rps_path.open() as rps_file:
        for line in rps_file.readlines():
            line = line.strip()
            if len(line) > 0:
                matches.append(Match(line))

    return matches


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
