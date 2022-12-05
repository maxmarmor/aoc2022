#!/usr/bin/python3

with open("input.txt", "r") as f:
    puzzle_input = f.read()

str_guide = [row.split(" ") for row in puzzle_input.split("\n")]

# Part 1
scores = {
    "A": 1,
    "B": 2,
    "C": 3,
    "X": 1,
    "Y": 2,
    "Z": 3,
}
outcomes = {
    "A": {"X": 3, "Y": 6, "Z": 0},
    "B": {"X": 0, "Y": 3, "Z": 6},
    "C": {"X": 6, "Y": 0, "Z": 3},
}
total_score_1 = 0
for row in str_guide:
    total_score_1 += scores[row[1]] + outcomes[row[0]][row[1]]
print("Total Score Part 1:", total_score_1)

# Part 2
outcomes_2 = {
    "A": {"X": 0 + 3, "Y": 3 + 1, "Z": 6 + 2},
    "B": {"X": 0 + 1, "Y": 3 + 2, "Z": 6 + 3},
    "C": {"X": 0 + 2, "Y": 3 + 3, "Z": 6 + 1},
}
total_score_2 = 0
for row in str_guide:
    total_score_2 += outcomes_2[row[0]][row[1]]
print("Total Score Part 2:", total_score_2)
