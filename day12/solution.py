#!/usr/bin/python3
from dataclasses import dataclass, field
import math

with open("input.txt", "r") as f:
    puzzle_input = f.read()

Input: list[str] = puzzle_input.split("\n")


@dataclass
class Square:
    coordinates: tuple
    height: int = math.inf
    visited: bool = False
    adjacent_squares: list = field(default_factory=list)
    distance: int = math.inf

    def get_neighbor(self, direction) -> tuple:
        return tuple(map(lambda x, y: x + y, self.coordinates, direction))


def get_square_w_min_distance(neighbours):
    min_dist = math.inf
    next_target = None
    for coordinates in neighbours:
        square = squares[coordinates]
        if not square.visited and square.distance < min_dist:
            min_dist = square.distance
            next_target = square
    return next_target


def dijkstra(current_square: Square):
    current_square.visited = True
    for coordinates in current_square.adjacent_squares:
        adj_square = squares[coordinates]
        if adj_square.distance > current_square.distance + 1:
            adj_square.distance = current_square.distance + 1


start_square: Square
target_square: Square
heights = "abcdefghijklmnopqrstuvwxyz"
directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

# Part 1
squares = {}

for r in range(len(Input)):
    for c in range(len(Input[0])):
        value = Input[r][c]
        squares[(c, r)] = Square((c, r))
        if value not in "SE":
            squares[(c, r)].height = heights.index(value)
        elif value == "S":
            start_square = squares[(c, r)]
            squares[(c, r)].height = heights.index("a")
            squares[(c, r)].distance = 0
        elif value == "E":
            target_square = squares[(c, r)]
            squares[(c, r)].height = heights.index("z")
        else:
            print("Wrong input:", value)

for c, s in squares.items():
    for d in directions:
        check_coord = s.get_neighbor(d)
        if check_coord in squares and squares[check_coord].height <= s.height + 1:
            s.adjacent_squares.append(squares[check_coord].coordinates)

while True:
    next_square = get_square_w_min_distance(squares.keys())
    if not next_square:
        break
    dijkstra(next_square)

print("Result Part 1:", target_square.distance)


# Part 2
squares = {}

for r in range(len(Input)):
    for c in range(len(Input[0])):
        value = Input[r][c]
        squares[(c, r)] = Square((c, r))
        if value not in "SE":
            squares[(c, r)].height = heights.index(value)
        elif value == "S":
            squares[(c, r)].height = heights.index("a")
        elif value == "E":
            start_square = squares[(c, r)]
            squares[(c, r)].height = heights.index("z")
            squares[(c, r)].distance = 0
        else:
            print("Wrong input:", value)

for c, s in squares.items():
    for d in directions:
        check_coord = s.get_neighbor(d)
        if check_coord in squares and squares[check_coord].height >= s.height - 1:
            s.adjacent_squares.append(squares[check_coord].coordinates)

while True:
    next_square = get_square_w_min_distance(squares.keys())
    if not next_square:
        break
    dijkstra(next_square)

min_distance = math.inf
for c, s in squares.items():
    if s.height == 0 and s.distance < min_distance:
        min_distance = s.distance

print("Result Part 2:", min_distance)
