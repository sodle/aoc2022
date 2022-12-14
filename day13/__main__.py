# Day 13: Distress Signal
from pathlib import Path
import json

from typing import Union, Optional


def compare_packets(left: list[Union[int, list]], right: list[Union[int, list]]) -> Optional[bool]:
    # if left is empty but right isn't, we're definitely in order
    if len(left) == 0 and len(right) > 0:
        return True

    for index, left_value in enumerate(left):
        if index >= len(right):
            return False

        right_value = right[index]

        if left_value == right_value:
            continue

        # both are ints, so just compare them
        if isinstance(left_value, int) and isinstance(right_value, int):
            if left_value != right_value:
                # if the values are different, compare them and decide if we're in order, otherwise keep going
                return left_value < right_value
            else:
                continue

        # at least one is list, so make sure they both are, and recurse
        if not isinstance(left_value, list):
            left_value = [left_value]
        if not isinstance(right_value, list):
            right_value = [right_value]

        if isinstance(left_value, list) and isinstance(right_value, list):
            compare = compare_packets(left_value, right_value)
            if compare is not None:
                return compare

    # if none of the previous checks fail, we're in order!
    return True


def part1(lines: list[str]) -> int:
    ordered_indices = []
    index = 1

    pair = []
    for line in lines:
        line = line.strip()
        if len(line) == 0:
            continue

        pair.append(json.loads(line))
        if len(pair) == 2:
            if compare_packets(*pair):
                ordered_indices.append(index)

            pair = []
            index += 1

    return sum(ordered_indices)


def part2(lines: list[str]) -> int:
    return 0


if __name__ == "__main__":
    input_path = Path(__file__).parent.joinpath("input.txt")
    with input_path.open() as input_file:
        input_lines = input_file.readlines()
        print(f"Part 1:\t{part1(input_lines)}")
        print(f"Part 2:\t{part2(input_lines)}")
