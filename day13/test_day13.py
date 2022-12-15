from pathlib import Path

from day13.__main__ import part1, part2


def test_part1():
    with Path(__file__).parent.joinpath("test_input").joinpath("packets.txt").open() as input_file:
        assert part1(input_file.readlines()) == 13


def test_part2():
    with Path(__file__).parent.joinpath("test_input").joinpath("packets.txt").open() as input_file:
        assert part2(input_file.readlines()) == 140
