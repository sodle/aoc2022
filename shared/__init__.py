from pathlib import Path

from typing import List


def parse_elves(elf_path: Path) -> List[List[int]]:
    # Parse each elf's bounty into a list of fruits, and return the full list of elves
    elves = []
    current_elf = []

    with elf_path.open() as elf_file:
        for line in elf_file.readlines():
            line = line.strip()
            if len(line) > 0:
                current_elf.append(int(line))
            else:
                elves.append(current_elf)
                current_elf = []

    if len(current_elf) > 0:
        elves.append(current_elf)

    return elves
