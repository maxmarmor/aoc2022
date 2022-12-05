#!/usr/bin/python3

with open("input.txt", "r") as f:
    puzzle_input = f.read()

# Part 1 and 2
elves = puzzle_input.split("\n\n")
elves_sums = sorted(
    [sum([int(cal) for cal in cals]) for cals in [elf.split("\n") for elf in elves]]
)
print("Max cals:", max(elves_sums))
print("Sum of three max cals:", sum(elves_sums[-3:]))
