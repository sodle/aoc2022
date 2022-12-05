from pathlib import Path

from day05.__main__ import part1, part2, Crane

input_path = Path(__file__).parent.joinpath("test_data").joinpath("crane.txt")


def test_part1():
    assert part1(input_path) == "CMZ"


def test_part2():
    assert part2(input_path) == "MCD"


test_data_path = Path(__file__).parent.joinpath("test_data")


def test_parse():
    crane = Crane(test_data_path.joinpath("crane.txt"))
    assert len(crane.stacks[1]) == 2
    assert len(crane.stacks[2]) == 3
    assert len(crane.stacks[3]) == 1


def test_toppers():
    crane = Crane(test_data_path.joinpath("crane.txt"))
    assert crane.toppers() == ["N", "D", "P"]


def test_run_crane():
    crane = Crane(test_data_path.joinpath("crane.txt"))
    crane.run_crane()
    assert crane.toppers() == ["C", "M", "Z"]
