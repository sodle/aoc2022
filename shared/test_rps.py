from pathlib import Path

from shared.rps import parse

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
