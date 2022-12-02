from shared.rps import Match

from day02.__main__ import part1, part2

test_input = [
    Match("A Y"),
    Match("B X"),
    Match("C Z"),
]


def test_part1():
    assert part1(test_input) == 15


def test_part2():
    assert part2(test_input) == 12
