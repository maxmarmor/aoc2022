#!/usr/bin/python3
from functools import cmp_to_key

with open("input.txt", "r") as f:
    puzzle_input = f.read()

Input: list[str] = puzzle_input.split("\n\n")


def get_closing_bracket_index(text):
    open_brackets = 1
    for i in range(1, len(text)):
        if text[i] == "[":
            open_brackets += 1
        elif text[i] == "]":
            open_brackets -= 1
        if open_brackets == 0:
            return i
    print("No closing bracket found!")


def check_pair(l, r):
    if l == "" and r == "":
        return "continue"
    elif l == "":
        return "right order"
    elif r == "":
        return "wrong order"

    if l[0] == "[" or r[0] == "[":
        next_l = l.split(",")[0]
        next_r = r.split(",")[0]
        end_l = len(next_l) - 1
        end_r = len(next_r) - 1
        if l[0] == "[":
            end_l = get_closing_bracket_index(l)
            next_l = l[1:end_l]
        if r[0] == "[":
            end_r = get_closing_bracket_index(r)
            next_r = r[1:end_r]
        res = check_pair(next_l, next_r)
        if res == "continue":
            next_l = l[end_l+1:]
            next_r = r[end_r+1:]
            return check_pair(next_l, next_r)
        else:
            return res
    if l[0] == "," and r[0] == ",":
        return check_pair(l[1:], r[1:])
    next_l = l.split(",")
    next_r = r.split(",")
    if int(next_l[0]) < int(next_r[0]):
        return "right order"
    elif int(next_l[0]) > int(next_r[0]):
        return "wrong order"
    elif int(next_l[0]) == int(next_r[0]):
        return check_pair(",".join(next_l[1:]), ",".join(next_r[1:]))

    print("Something went wrong:", next_l, next_r)


# Part 1
total = 0
for pair_index in range(len(Input)):
    left, right = Input[pair_index].split("\n")
    if check_pair(left, right) == "right order":
        total += pair_index + 1

print("Result Part 1:", total)


# Part 2
def cmp(l, r):
    if check_pair(l, r) == "right order":
        return 1
    else:
        return -1


Input = "\n".join(Input).split("\n")
sorted_input = list(reversed(sorted(Input + ["[[2]]"] + ["[[6]]"], key=cmp_to_key(cmp))))
print("Result Part 2:", (sorted_input.index("[[2]]") + 1) * (sorted_input.index("[[6]]") + 1))
