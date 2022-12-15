#!/usr/bin/python3

with open("input.txt", "r") as f:
    puzzle_input = f.read()

Input: list[str] = puzzle_input.split("\n")


def dist(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


sensors = {}
for row in Input:
    row = row.split(" ")
    sensor_pos = (int(row[2][2:-1]), int(row[3][2:-1]))
    beacon_pos = (int(row[8][2:-1]), int(row[9][2:]))
    sensors[sensor_pos] = [beacon_pos, dist(sensor_pos, beacon_pos)]


def combine(a, b):
    if (
            b[0] <= a[0] <= b[1]
            or a[0] <= b[0] <= a[1]
            or a[1] + 1 == b[0]
            or b[1] + 1 == a[0]
    ):
        return [min([a[0], b[0]]), max([a[1], b[1]])], []
    else:
        return a, b


def get_intervals_for_row(row_number) -> list:
    intervals = []
    for pos, [_, distance] in sensors.items():
        row_distance = abs(row_number - pos[1])
        if row_distance <= distance:
            intervals.append([pos[0] - (distance - row_distance), pos[0] + (distance - row_distance)])
    # print(intervals)

    while True:
        cnt_empty = 0
        for i in range(len(intervals) - 1):
            if not intervals[i]:
                continue
            for j in range(i+1, len(intervals)):
                if not intervals[j]:
                    continue
                a, b = combine(intervals[i], intervals[j])
                intervals[i] = a
                intervals[j] = b
        tmp_intervals = []
        for interval in intervals:
            if not interval:
                cnt_empty += 1
            else:
                tmp_intervals.append(interval)
        intervals = tmp_intervals
        if not cnt_empty:
            break
    return intervals


# Part 1
target_row = 2000000
row_intervals = get_intervals_for_row(target_row)
total = 0
beacons_on_target_row = set()
for _, data in sensors.items():
    if data[0][1] == target_row:
        beacons_on_target_row.add(data[0])
for row_interval in row_intervals:
    total += row_interval[1] - row_interval[0] + 1 - len(beacons_on_target_row)
print("Result Part 1:", total)


# Part 2
result = -1
multiplier = 4000000
for y in range(multiplier + 1):
    row_intervals = get_intervals_for_row(y)
    if len(row_intervals) > 1:
        x = min([row_intervals[0][1], row_intervals[1][1]]) + 1
        if not (0 <= x <= multiplier):
            continue
        result = x * multiplier + y
        break
print("Result Part 2:", result)
