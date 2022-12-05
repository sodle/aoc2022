from pathlib import Path

from day05.__main__ import part1, part2

input_path = Path(__file__).parent.parent.joinpath("shared").joinpath("test_data").joinpath("crane.txt")


def test_part1():
    assert part1(input_path) == "CMZ"


def test_part2():
    assert part2(input_path) == "MCD"
