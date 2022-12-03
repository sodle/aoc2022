from pathlib import Path

from shared.rucksack import parse, item_priority

test_data_path = Path(__file__).parent.joinpath("test_data")


def test_item_priority():
    assert item_priority("a") == 1
    assert item_priority("A") == 27


def test_parse_rucksacks():
    rucksacks = parse(test_data_path.joinpath("rucksacks.txt"))
    assert rucksacks[0].first_common_item() == "p"
    assert rucksacks[1].first_common_item() == "L"
    assert rucksacks[2].first_common_item() == "P"
    assert rucksacks[3].first_common_item() == "v"
    assert rucksacks[4].first_common_item() == "t"
    assert rucksacks[5].first_common_item() == "s"
