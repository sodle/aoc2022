from pathlib import Path

from day04.__main__ import part1, part2, Patrol, parse

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
