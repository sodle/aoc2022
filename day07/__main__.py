# Day 07: No Space Left On Device
from pathlib import Path

from pyfakefs.fake_filesystem import FakeFilesystem, FakeDirectory

from typing import List


def directory_sizer(directory: FakeDirectory, max_size: int = 100000) -> int:
    total_size = 0

    for entry in directory.entries.values():
        if isinstance(entry, FakeDirectory):
            if entry.size <= max_size:
                total_size += entry.size
            total_size += directory_sizer(entry, max_size=max_size)

    return total_size


def build_fake_filesystem(input_lines: List[str]) -> FakeFilesystem:
    fs = FakeFilesystem()
    program_counter = 0
    while program_counter < len(input_lines):
        line = input_lines[program_counter].strip()
        if line.startswith("$ cd "):
            _, _, dir_name = line.split()
            fs.cwd = Path(fs.cwd).joinpath(dir_name)
            program_counter += 1
        elif line == "$ ls":
            program_counter += 1
            line = input_lines[program_counter].strip()
            while not line.startswith("$ "):
                if line.startswith("dir "):
                    _, dir_name = line.split()
                    fs.makedir(Path(fs.cwd).joinpath(dir_name))
                else:
                    size_str, file_name = line.split()
                    fs.create_file(Path(fs.cwd).joinpath(file_name), st_size=int(size_str))
                program_counter += 1
                if program_counter >= len(input_lines):
                    break
                line = input_lines[program_counter].strip()
    return fs


def part1(input_lines: List[str]) -> int:
    fs = build_fake_filesystem(input_lines)
    return directory_sizer(fs.root)


def directory_sizer_2(directory: FakeDirectory, min_size: int) -> List[int]:
    directories = []

    if directory.size >= min_size:
        directories.append(directory.size)
        for entry in directory.entries.values():
            if isinstance(entry, FakeDirectory):
                directories.extend(directory_sizer_2(entry, min_size))

    return directories


def part2(input_lines: List[str]) -> int:
    fs = build_fake_filesystem(input_lines)

    free_space = 70000000 - fs.root.size
    space_to_reclaim = 30000000 - free_space

    directory_sizes = directory_sizer_2(fs.root, space_to_reclaim)
    return min(directory_sizes)


def main():
    input_path = Path(__file__).parent.joinpath("input.txt")
    with input_path.open() as input_file:
        input_lines = input_file.readlines()
        print(f"Part 1:\t{part1(input_lines)}")
        print(f"Part 2:\t{part2(input_lines)}")


if __name__ == "__main__":
    main()
