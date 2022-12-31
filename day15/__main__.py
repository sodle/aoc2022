# Day 15: Beacon Exclusion Zone
from pathlib import Path
import re

scan_regex = re.compile(r'Sensor at x=(?P<sensor_x>-?\d+), y=(?P<sensor_y>-?\d+): '
                        r'closest beacon is at x=(?P<beacon_x>-?\d+), y=(?P<beacon_y>-?\d+)')


def part1(lines: list[str], check_row: int = 2000000) -> int:
    beacons_in_row = set()
    covered_points_in_row = set()

    for line in lines:
        line = line.strip()
        if len(line) > 0:
            sensor_x, sensor_y, beacon_x, beacon_y = scan_regex.fullmatch(line).groups()

            sensor_x = int(sensor_x)
            sensor_y = int(sensor_y)
            beacon_x = int(beacon_x)
            beacon_y = int(beacon_y)

            if beacon_y == check_row:
                beacons_in_row.add(beacon_x)

            sensor_range = abs(sensor_x - beacon_x) + abs(sensor_y - beacon_y)
            distance_to_check_row = abs(check_row - sensor_y)

            if distance_to_check_row <= sensor_range:
                x_range = sensor_range - distance_to_check_row
                covered_points_in_row = covered_points_in_row.union(set(range(sensor_x - x_range,
                                                                              sensor_x + x_range + 1)))

    return len(covered_points_in_row - beacons_in_row)


def part2(lines: list[str], bound: int = 4000000) -> int:
    exclusions: list[set[int]] = [set() for _ in range(bound + 1)]

    bounding_set = set(range(bound + 1))
    for line in lines:
        line = line.strip()
        if len(line) > 0:
            sensor_x, sensor_y, beacon_x, beacon_y = scan_regex.fullmatch(line).groups()

            sensor_x = int(sensor_x)
            sensor_y = int(sensor_y)
            beacon_x = int(beacon_x)
            beacon_y = int(beacon_y)

            if beacon_x in range(bound + 1) and beacon_y in range(bound + 1):
                exclusions[beacon_y].add(beacon_x)

            sensor_range = abs(sensor_x - beacon_x) + abs(sensor_y - beacon_y)

            columns = list(range(sensor_x - sensor_range, sensor_x + sensor_range + 1))
            for row in range(sensor_range + 1):

                up = sensor_y - row
                down = sensor_y + row

                column_set = set(columns).intersection(bounding_set)

                if up in bounding_set:
                    exclusions[up] = exclusions[up].union(column_set)
                if down in bounding_set:
                    exclusions[down] = exclusions[down].union(column_set)

                columns.pop()

                if len(columns) > 0:
                    columns.pop(0)

    for y, row in enumerate(exclusions):
        if len(row) == bound:
            x = (bounding_set - row).pop()
            return x * 4000000 + y

    return 0


if __name__ == "__main__":
    input_path = Path(__file__).parent.joinpath("test_input").joinpath("test_input.txt")
    with input_path.open() as input_file:
        input_lines = input_file.readlines()
        # print(f"Part 1:\t{part1(input_lines, check_row=10)}")
        print(f"Part 2:\t{part2(input_lines, bound=20)}")
