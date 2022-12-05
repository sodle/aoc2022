# Day 05: Supply Stacks
from pathlib import Path

from shared.crane import Crane


def part1(input_path: Path) -> str:
    crane = Crane(input_path)
    crane.run_crane()
    return "".join(crane.toppers())


def part2(input_path: Path) -> str:
    crane = Crane(input_path)
    crane.run_crane_9001()
    return "".join(crane.toppers())


def main():
    input_path = Path(__file__).parent.joinpath("input.txt")
    print(f"Part 1:\t{part1(input_path)}")
    print(f"Part 2:\t{part2(input_path)}")


if __name__ == "__main__":
    main()
