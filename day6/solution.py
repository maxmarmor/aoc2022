#!/usr/bin/python3

with open("input.txt", "r") as f:
    puzzle_input = f.read()

messages = puzzle_input.split("\n")

# Part 1
for message in messages:
    for pos in range(3, len(message)):
        cur_slice = message[pos-3:pos+1]
        if len(cur_slice) == len(set(cur_slice)):
            print("Result Part 1:", pos+1)
            break

# Part 2
for message in messages:
    for pos in range(13, len(message)):
        cur_slice = message[pos-13:pos+1]
        if len(cur_slice) == len(set(cur_slice)):
            print("Result Part 2:", pos+1)
            break
