from day01.__main__ import part1, part2

test_input = [
    [1000, 2000, 3000],
    [4000],
    [5000, 6000],
    [7000, 8000, 9000],
    [10000],
]


def test_part1():
    assert part1(test_input) == 24000


def test_part2():
    assert part2(test_input) == 45000
