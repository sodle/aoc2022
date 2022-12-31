# Day 15: Beacon Exclusion Zone
from pathlib import Path
import re
import random
import threading

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
    sensors = []
    for line in lines:
        line = line.strip()
        match = scan_regex.fullmatch(line)
        if match is not None:
            sensor_x, sensor_y, beacon_x, beacon_y = [int(g) for g in match.groups()]
            sensor_range = abs(sensor_x - beacon_x) + abs(sensor_y - beacon_y)
            sensors.append((sensor_x, sensor_y, sensor_range))

    for sensor_x, sensor_y, sensor_range in sensors:
        scan_radius = sensor_range + 1
        scan_x = scan_radius
        scan_y = 0

        while scan_x >= scan_y:
            for check_x, check_y in [
                (sensor_x + scan_x, sensor_y + scan_y),
                (sensor_x - scan_x, sensor_y + scan_y),
                (sensor_x + scan_x, sensor_y - scan_y),
                (sensor_x - scan_x, sensor_y - scan_y),
            ]:
                if 0 <= check_x <= bound and 0 <= check_y <= bound:
                    for other_x, other_y, other_range in sensors:
                        if abs(check_x - other_x) + abs(check_y - other_y) <= other_range:
                            break
                    else:
                        return check_x * 4000000 + check_y

            scan_x -= 1
            scan_y += 1


if __name__ == "__main__":
    input_path = Path(__file__).parent.joinpath("input.txt")
    with input_path.open() as input_file:
        input_lines = input_file.readlines()
        print(f"Part 1:\t{part1(input_lines)}")
        print(f"Part 2:\t{part2(input_lines)}")
