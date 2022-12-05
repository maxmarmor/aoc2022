#!/usr/bin/python3

with open("input.txt", "r") as f:
    puzzle_input = f.read()

pairs = puzzle_input.split("\n")
pairs = [[[int(i) for i in sec.split("-")] for sec in pair.split(",")] for pair in pairs]

# Part 1
total = 0
for sec_1, sec_2 in pairs:
    if (sec_1[0] >= sec_2[0] and sec_1[1] <= sec_2[1]) or (
        sec_2[0] >= sec_1[0] and sec_2[1] <= sec_1[1]
    ):
        total += 1
print("Num pairs Part 1:", total)

# Part 2
total = 0
for sec_1, sec_2 in pairs:
    sec_1 = set(range(sec_1[0], sec_1[1] + 1))
    sec_2 = set(range(sec_2[0], sec_2[1] + 1))
    if len(sec_1.intersection(sec_2)) > 0:
        total += 1
print("Num pairs Part 2:", total)
