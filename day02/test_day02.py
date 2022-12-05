from pathlib import Path

from day02.__main__ import part1, part2, Match, parse

test_input = [
    Match("A Y"),
    Match("B X"),
    Match("C Z"),
]


def test_part1():
    assert part1(test_input) == 15


def test_part2():
    assert part2(test_input) == 12


test_data_path = Path(__file__).parent.joinpath("test_data")


def test_parse():
    matches = parse(test_data_path.joinpath("rps_matches.txt"))
    assert matches[0].score() == 8
    assert matches[1].score() == 1
    assert matches[2].score() == 6


def test_throw():
    matches = parse(test_data_path.joinpath("rps_matches.txt"))
    assert matches[0].throw() == 4
    assert matches[1].throw() == 1
    assert matches[2].throw() == 7
