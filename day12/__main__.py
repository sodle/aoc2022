# Day 12: Hill Climbing Algorithm
import string
from pathlib import Path

from networkx import DiGraph, shortest_path_length, NetworkXNoPath


def letter_height(letter: str) -> int:
    if letter == "S":
        return 0
    if letter == "E":
        return 25
    return string.ascii_lowercase.index(letter)


def node_name(row_num: int, col_num: int, letter: str) -> str:
    if letter in "SE":
        return letter
    return f"{letter},{row_num},{col_num}"


def parse_hill(lines: list[str]) -> DiGraph:
    g = DiGraph()

    for row_num, line in enumerate(lines):
        for col_num, letter in enumerate(line):
            if letter not in string.ascii_letters:
                continue

            node = node_name(row_num, col_num, letter)
            height = letter_height(letter)

            if row_num > 0 and len(lines[row_num - 1]) > col_num:
                up_letter = lines[row_num - 1][col_num]
                if up_letter in string.ascii_letters:
                    up_height = letter_height(up_letter)
                    if up_height <= height + 1:
                        up_node = node_name(row_num - 1, col_num, up_letter)
                        g.add_edge(node, up_node)

            if col_num > 0:
                left_letter = line[col_num - 1]
                if left_letter in string.ascii_letters:
                    left_height = letter_height(left_letter)
                    if left_height <= height + 1:
                        left_node = node_name(row_num, col_num - 1, left_letter)
                        g.add_edge(node, left_node)

            if row_num < len(lines) - 1 and len(lines[row_num + 1]) > col_num:
                down_letter = lines[row_num + 1][col_num]
                if down_letter in string.ascii_letters:
                    down_height = letter_height(down_letter)
                    if down_height <= height + 1:
                        down_node = node_name(row_num + 1, col_num, down_letter)
                        g.add_edge(node, down_node)

            if col_num < len(line) - 1:
                right_letter = line[col_num + 1]
                if right_letter in string.ascii_letters:
                    right_height = letter_height(right_letter)
                    if right_height <= height + 1:
                        right_node = node_name(row_num, col_num + 1, right_letter)
                        g.add_edge(node, right_node)

    return g


def part1(lines: list[str]) -> int:
    g = parse_hill(lines)
    return shortest_path_length(g, source="S", target="E")


def part2(lines: list[str]) -> int:
    g = parse_hill(lines)

    candidate_paths = [
        shortest_path_length(g, source="S", target="E")
    ]
    for node in g.nodes:
        if node.startswith("a"):
            try:
                candidate_paths.append(shortest_path_length(g, source=node, target="E"))
            except NetworkXNoPath:
                pass

    return min(candidate_paths)


if __name__ == "__main__":
    input_path = Path(__file__).parent.joinpath("input.txt")
    with input_path.open() as input_file:
        input_lines = input_file.readlines()
        print(f"Part 1:\t{part1(input_lines)}")
        print(f"Part 2:\t{part2(input_lines)}")
