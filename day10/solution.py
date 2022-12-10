#!/usr/bin/python3

with open("input.txt", "r") as f:
    puzzle_input = f.read()


Input: list[str] = puzzle_input.split("\n")
X: int = 1
cycle: int = 0
signal_strength = 0
output: list = []


def draw_sprite():
    if cycle % 40 == 1:
        output.append("")
    crt_position = (cycle - 1) % 40
    if X - 1 <= crt_position <= X + 1:
        output[-1] += "#"
    else:
        output[-1] += "."


def add_cycle():
    global cycle, signal_strength, X
    cycle += 1
    draw_sprite()
    if (cycle - 20) % 40 == 0:
        signal_strength += X * cycle


# Part 1 & 2
for instruction in Input:
    add_cycle()
    instruction = instruction.split(" ")
    if instruction[0] == "addx":
        add_cycle()
        X += int(instruction[1])


print("Result Part 1:", signal_strength)
print("Result Part 2:", "\n" + "\n".join(output))
