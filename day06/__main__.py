# Day 06: Tuning Trouble
from pathlib import Path


def part1(input_line: str) -> int:
    for start_index in range(len(input_line)):
        end_index = start_index + 4
        char_set = set(input_line[start_index:end_index])
        if len(char_set) == 4:
            return end_index
    return -1


def part2(input_line: str) -> int:
    for start_index in range(len(input_line)):
        end_index = start_index + 14
        char_set = set(input_line[start_index:end_index])
        if len(char_set) == 14:
            return end_index
    return -1


def main():
    input_path = Path(__file__).parent.joinpath("input.txt")
    with input_path.open() as input_file:
        input_line = input_file.readline().strip()
        print(f"Part 1:\t{part1(input_line)}")
        print(f"Part 2:\t{part2(input_line)}")


if __name__ == "__main__":
    main()
