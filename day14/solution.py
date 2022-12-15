#!/usr/bin/python3

with open("input.txt", "r") as f:
    puzzle_input = f.read()

Input: list[str] = puzzle_input.split("\n")

grid = {}  # {x: set(y_coords)}
sand = {}  # {x: set(y_coords)}


def calc_ranges(current_grid, current_sand):
    x_vals = list(current_grid.keys()) + list(current_sand.keys())
    _max_y = 0
    for _, _y in grid.items():
        if len(_y) == 0:
            continue
        if max(_y) > _max_y:
            _max_y = max(_y)
    return [min(x_vals), max(x_vals)], [0, _max_y + 4]


def print_grid(current_grid, current_sand, show_bottom=False):
    x_range, y_range = calc_ranges(current_grid, current_sand)
    grid_map = []
    for _ in range(0, max_y + 2):
        grid_map.append("")
        for _ in range(x_range[1] - x_range[0] + 1):
            grid_map[-1] += "."
    for _x, y_s in current_grid.items():
        for _y in y_s:
            grid_map[_y] = (
                    grid_map[_y][:_x - x_range[0]]
                    + "#"
                    + grid_map[_y][_x - x_range[0] + 1:]
            )
    for _x, y_s in current_sand.items():
        for _y in y_s:
            grid_map[_y] = (
                    grid_map[_y][:_x - x_range[0]]
                    + "O"
                    + grid_map[_y][_x - x_range[0] + 1:]
            )
    if show_bottom:
        grid_map.append("")
        for _ in range(x_range[1] - x_range[0] + 1):
            grid_map[-1] += "#"

    print("\n".join(grid_map))


def move_sand(coord):
    global grid, sand
    x = coord[0]
    y = coord[1]
    if x not in grid:
        grid[x] = set()
    if x not in sand:
        sand[x] = set()
    if (y + 1) in grid[x] or (y + 1) in sand[x]:
        if x - 1 not in grid.keys():
            grid[x-1] = set()
        if x - 1 not in sand.keys():
            sand[x-1] = set()
        if x + 1 not in grid.keys():
            grid[x+1] = set()
        if x + 1 not in sand.keys():
            sand[x+1] = set()
        if (y + 1) not in grid[x-1] and (y + 1) not in sand[x-1]:
            return x - 1, y + 1
        if (y + 1) not in grid[x+1] and (y + 1) not in sand[x+1]:
            return x + 1, y + 1
    else:
        return x, min([next_y for next_y in grid[x].union(sand[x]) if next_y > y] + [max_y+2]) - 1
    return coord


for row in Input:
    points = [list(map(int, point.split(","))) for point in row.split(" -> ")]
    for i in range(1, len(points)):
        start = points[i-1]
        end = points[i]
        if start[0] not in grid.keys():
            grid[start[0]] = set()
        if end[0] not in grid.keys():
            grid[end[0]] = set()
        if start[0] == end[0]:
            for y in range(min([start[1], end[1]]), max([start[1], end[1]]) + 1):
                grid[start[0]].add(y)
        elif start[1] == end[1]:
            for x in range(min([start[0], end[0]]), max([start[0], end[0]]) + 1):
                if x not in grid.keys():
                    grid[x] = set()
                grid[x].add(start[1])

max_y = 0
for _, y in grid.items():
    if max(y) > max_y:
        max_y = max(y)


starting_coord = (500, 0)
while True:
    current_coord = starting_coord
    while True:
        new_coord = move_sand(current_coord)
        if new_coord == current_coord:
            sand[new_coord[0]].add(new_coord[1])
            break
        current_coord = new_coord
        if new_coord[1] >= max_y:
            break
    if current_coord[1] >= max_y:
        break
print_grid(grid, sand)
print("Result Part 1:", sum([len(s) for _, s in sand.items()]))

# # Part 2
sand = {}
while True:
    current_coord = starting_coord
    while True:
        new_coord = move_sand(current_coord)
        if new_coord == current_coord:
            sand[new_coord[0]].add(new_coord[1])
            break
        current_coord = new_coord
        if new_coord[1] == max_y + 1:
            sand[new_coord[0]].add(new_coord[1])
            break
    if current_coord == starting_coord or len(sand) > 10000:
        break

print_grid(grid, sand, True)
print("Result Part 2:", sum([len(s) for _, s in sand.items()]))
