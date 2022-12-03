from shared.rucksack import Rucksack

from day03.__main__ import part1, part2

test_input = [
    Rucksack("vJrwpWtwJgWrhcsFMMfFFhFp"),
    Rucksack("jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL"),
    Rucksack("PmmdzqPrVvPwwTWBwg"),
    Rucksack("wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn"),
    Rucksack("ttgJtRGJQctTZtZT"),
    Rucksack("CrZsJsPPZsGzwwsLwLmpwMDw"),
]


def test_part1():
    assert part1(test_input) == 157


def test_part2():
    assert part2(test_input) == 70
