from shared.patrols import Patrol

from day04.__main__ import part1, part2

test_input = [
    Patrol("2-4,6-8"),
    Patrol("2-3,4-5"),
    Patrol("5-7,7-9"),
    Patrol("2-8,3-7"),
    Patrol("6-6,4-6"),
    Patrol("2-6,4-8"),
]


def test_part1():
    assert part1(test_input) == 2


def test_part2():
    assert part2(test_input) == 4
