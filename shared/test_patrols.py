from pathlib import Path

from shared.patrols import parse

test_data_path = Path(__file__).parent.joinpath("test_data")


def test_parse():
    patrols = parse(test_data_path.joinpath("patrols.txt"))
    assert not patrols[0].has_total_overlap()
    assert not patrols[1].has_total_overlap()
    assert not patrols[2].has_total_overlap()
    assert patrols[3].has_total_overlap()
    assert patrols[4].has_total_overlap()
    assert not patrols[5].has_total_overlap()


def test_overlap():
    patrols = parse(test_data_path.joinpath("patrols.txt"))
    assert not patrols[0].has_any_overlap()
    assert not patrols[1].has_any_overlap()
    assert patrols[2].has_any_overlap()
    assert patrols[3].has_any_overlap()
    assert patrols[4].has_any_overlap()
    assert patrols[5].has_any_overlap()
