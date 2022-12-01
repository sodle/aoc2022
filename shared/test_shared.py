from pathlib import Path

from shared import parse_elves

test_data_path = Path(__file__).parent.joinpath("test_data")

expected_elves = [
    [1000, 2000, 3000],
    [4000],
    [5000, 6000],
    [7000, 8000, 9000],
    [10000],
]


def test_parse_elves():
    assert parse_elves(test_data_path.joinpath("elves.txt")) == expected_elves
    assert parse_elves(test_data_path.joinpath("elves_no_newline.txt")) == expected_elves
