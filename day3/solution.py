#!/usr/bin/python3

with open("input.txt", "r") as f:
    puzzle_input = f.read()

rucksacks = puzzle_input.split("\n")
chrs = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

# Part 1
total = 0
for rucksack in rucksacks:
    length = len(rucksack)
    for shared_item in set(rucksack[: int(length / 2)]).intersection(
        set(rucksack[int(length / 2):])
    ):
        total += chrs.index(shared_item) + 1
print("Sum Part 1:", total)

# Part 2
total = 0
for index in range(2, len(rucksacks), 3):
    for shared_item in set(rucksacks[index - 2]).intersection(
        set(rucksacks[index - 1]).intersection(set(rucksacks[index]))
    ):
        total += chrs.index(shared_item) + 1
print("Sum Part 2:", total)
