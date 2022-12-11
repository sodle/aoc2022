# Day 11: Monkey in the Middle
import operator
from pathlib import Path

from typing import Optional


class Monkey:
    items: list[int]

    worry_operator: operator
    worry_operand: Optional[int]

    test: int
    if_true: int
    if_false: int

    inspect_count: int

    gcd: int = 1

    def __init__(self):
        self.inspect_count = 0

    def inspect_items(self, anxious: bool = False) -> list[tuple[int, int]]:
        throws = []

        while len(self.items) > 0:
            old_worry = self.items.pop(0)

            operand = self.worry_operand if self.worry_operand is not None else old_worry
            new_worry = self.worry_operator(old_worry, operand)

            if not anxious:
                new_worry //= 3

            if new_worry % self.test == 0:
                next_monkey = self.if_true
                new_worry %= self.gcd
            else:
                next_monkey = self.if_false

            self.inspect_count += 1

            throws.append((new_worry, next_monkey))

        return throws


def parse_monkeys(lines):
    monkeys = []
    current_monkey = None
    for line in lines:
        line = line.strip()
        if line.startswith("Monkey"):
            if current_monkey is not None:
                monkeys.append(current_monkey)
            current_monkey = Monkey()
        elif line.startswith("Starting"):
            _, items_str = line.split(": ")
            items = items_str.split(", ")
            current_monkey.items = [int(item) for item in items]
        elif line.startswith("Operation"):
            _, operation = line.split(" = ")
            _, worry_operator, worry_operand = operation.split()
            if worry_operator == "*":
                current_monkey.worry_operator = operator.mul
            elif worry_operator == "+":
                current_monkey.worry_operator = operator.add
            current_monkey.worry_operand = None if worry_operand == "old" else int(worry_operand)
        elif line.startswith("Test"):
            current_monkey.test = int(line.split()[-1])
            Monkey.gcd *= current_monkey.test
        elif line.startswith("If true"):
            current_monkey.if_true = int(line.split()[-1])
        elif line.startswith("If false"):
            current_monkey.if_false = int(line.split()[-1])
        elif current_monkey is not None:
            monkeys.append(current_monkey)
            current_monkey = None
    if current_monkey is not None:
        monkeys.append(current_monkey)
    return monkeys


def part1(lines: list[str]) -> int:
    Monkey.gcd = 1

    monkeys = parse_monkeys(lines)

    for _ in range(20):
        for monkey in monkeys:
            throws = monkey.inspect_items()
            for worry, next_monkey in throws:
                monkeys[next_monkey].items.append(worry)

    inspect_counts = sorted([monkey.inspect_count for monkey in monkeys], reverse=True)

    return inspect_counts[0] * inspect_counts[1]


def part2(lines: list[str]) -> int:
    Monkey.gcd = 1

    monkeys = parse_monkeys(lines)

    for round_number in range(10000):
        for monkey in monkeys:
            throws = monkey.inspect_items(anxious=True)
            for worry, next_monkey in throws:
                monkeys[next_monkey].items.append(worry)

    inspect_counts = sorted([monkey.inspect_count for monkey in monkeys], reverse=True)

    return inspect_counts[0] * inspect_counts[1]


if __name__ == "__main__":
    input_path = Path(__file__).parent.joinpath("input.txt")
    with input_path.open() as input_file:
        input_lines = input_file.readlines()
        print(f"Part 1:\t{part1(input_lines)}")
        print(f"Part 2:\t{part2(input_lines)}")
