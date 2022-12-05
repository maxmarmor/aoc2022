#!/usr/bin/python3

with open("input.txt", "r") as f:
    puzzle_input = f.read()

state, proc = puzzle_input.split("\n\n")
num_stacks = max([int(i) for i in state.split("\n")[-1].split(" ") if len(i) > 0])

# Part 1
stacks = [[] for _ in range(num_stacks)]
for row in state.split("\n")[:-1]:
    for i in range(0, len(row), 4):
        value = row[i+1:i+2]
        if value != " ":
            stacks[int(i/4)].insert(0, value)

for row in proc.split("\n"):
    exec_plan = row.split(" ")
    cnt = int(exec_plan[1])
    stack_from = int(exec_plan[3]) - 1
    stack_to = int(exec_plan[5]) - 1
    for _ in range(cnt):
        tmp_crate = stacks[stack_from].pop()
        stacks[stack_to].append(tmp_crate)

result = ""
for stack in stacks:
    result += stack[-1]
print("Result Part 1:", result)


# Part 2
stacks = [[] for _ in range(num_stacks)]
for row in state.split("\n")[:-1]:
    for i in range(0, len(row), 4):
        value = row[i+1:i+2]
        if value != " ":
            stacks[int(i/4)].insert(0, value)

for row in proc.split("\n"):
    exec_plan = row.split(" ")
    cnt = int(exec_plan[1])
    stack_from = int(exec_plan[3]) - 1
    stack_to = int(exec_plan[5]) - 1
    stacks[stack_to].extend(stacks[stack_from][-cnt:])
    stacks[stack_from] = stacks[stack_from][:-cnt]

result = ""
for stack in stacks:
    result += stack[-1]
print("Result Part 2:", result)