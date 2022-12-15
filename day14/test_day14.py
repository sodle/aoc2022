from pathlib import Path

from day14.__main__ import part1, part2


def test_part1():
    with Path(__file__).parent.joinpath("test_input").joinpath("test_input.txt").open() as input_file:
        assert part1(input_file.readlines()) == 24


def test_part2():
    with Path(__file__).parent.joinpath("test_input").joinpath("test_input.txt").open() as input_file:
        assert part2(input_file.readlines()) == 93
