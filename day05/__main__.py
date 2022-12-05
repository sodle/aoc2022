# Day 05: Supply Stacks
from pathlib import Path
from typing import Dict, List


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


class Crane:
    stacks: Dict[int, List[str]]
    stack_columns: Dict[int, int]

    crane_instructions: List[str]

    def __init__(self, input_path: Path):
        self.stacks = {}
        self.stack_columns = {}
        self.crane_instructions = []

        container_lines: List[str] = []

        with input_path.open() as input_file:
            for line in input_file.readlines():
                if len(line.strip()) == 0:
                    # Skip blank lines.
                    continue

                if "[" in line:
                    # This line is part of the stack of containers. We'll parse it later.
                    container_lines.append(line.rstrip())

                if line.lstrip()[0].isdigit():
                    # This is the line that shows us which column each stack of containers is in.
                    for column, stack in enumerate(line):
                        if str.isdigit(stack):
                            self.stack_columns[int(stack)] = column
                            self.stacks[int(stack)] = []

                if line.startswith("move"):
                    # This is an instruction for the crane.
                    self.crane_instructions.append(line.strip())

        for line in reversed(container_lines):
            # Parse the container lines, backwards, to form stacks.
            for stack, column in self.stack_columns.items():
                if column < len(line):
                    letter = line[column]
                    if letter.isalpha():
                        self.stacks[stack].append(letter)

    def run_crane(self):
        for instruction in self.crane_instructions:
            _, count, _, source, _, dest = instruction.split()
            count = int(count)
            source = int(source)
            dest = int(dest)

            for _ in range(count):
                container = self.stacks[source].pop()
                self.stacks[dest].append(container)

    def run_crane_9001(self):
        print(len(self.crane_instructions))
        for instruction in self.crane_instructions:
            _, count, _, source, _, dest = instruction.split()
            count = int(count)
            source = int(source)
            dest = int(dest)

            containers = self.stacks[source][-count:]
            try:
                assert len(containers) == count
            except AssertionError:
                pass
            self.stacks[source] = self.stacks[source][:-count]
            self.stacks[dest] += containers

            print(int(sum([len(s) for s in self.stacks.values()])))

    def toppers(self) -> List[str]:
        out = []
        for stack in sorted(self.stacks.keys()):
            out.append(self.stacks[stack][-1])
        return out
