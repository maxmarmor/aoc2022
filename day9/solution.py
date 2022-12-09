#!/usr/bin/python3

with open("input.txt", "r") as f:
    puzzle_input = f.read()

steps = [[el[0], int(el[1])] for el in
         [row.split(" ") for row in
          puzzle_input.split("\n")]]


def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def div(a, b):
    if a == 0:
        return 0
    return int(abs(a) // abs(b) * a / abs(a))


def move_tail(head, tail):
    diff = list(map(sub, head, tail))
    if max(map(abs, diff)) == 2:
        movement = list(map(div, diff, [2, 2]))
        tail = list(map(sub, head, movement))
    return tail


def move_head(head, tail, direction):
    directions = {
        "R": [1, 0],
        "L": [-1, 0],
        "U": [0, 1],
        "D": [0, -1],
    }
    movement = directions[direction]
    head = list(map(add, head, movement))
    tail = move_tail(head, tail)

    return head, tail


# Part 1
tail_positions = [(0, 0)]
pos_h, pos_t = [0, 0], [0, 0]
for step in steps:
    for i in range(step[1]):
        pos_h, pos_t = move_head(pos_h, pos_t, step[0])
        tail_positions.append(tuple(pos_t))

print("Result Part 1:", len(set(tail_positions)))

# Part 2
positions_of_nine = [(0, 0)]
current_positions = [[0, 0] for i in range(10)]
for step in steps:
    for i in range(step[1]):
        current_positions[0], current_positions[1] = move_head(current_positions[0], current_positions[1], step[0])
        for k in range(1, 9):
            current_positions[k + 1] = move_tail(current_positions[k], current_positions[k + 1])
        positions_of_nine.append(tuple(current_positions[9]))

print("Result Part 2:", len(set(positions_of_nine)))
