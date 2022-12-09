#!/usr/bin/python3

with open("input.txt", "r") as f:
    puzzle_input = f.read()

tree_map = puzzle_input.split("\n")
tree_map = [[int(row[i]) for i in range(len(row))] for row in tree_map]
len_x = len(tree_map[0])
len_y = len(tree_map)

# Part 1
visible_positions = []
for y in range(1, len_y - 1):
    for x in range(1, len_x - 1):
        max_left = max(tree_map[y][:x])
        max_right = max(tree_map[y][x+1:])
        max_up = max([row[x] for row in tree_map[:y]])
        max_down = max([row[x] for row in tree_map[y+1:]])
        if tree_map[y][x] > min(max_left, max_right, max_up, max_down):
            visible_positions.append([y, x])
total_visible = len(visible_positions) + 2*len_x + 2*(len_y - 2)
print("Result Part 1:", total_visible)


# Part 2
def count_trees(trees, direction, size):
    if len(trees) == 0:
        return 0
    total = 0
    if direction == -1:
        trees = reversed(trees)
    for tree in trees:
        total += 1
        if tree >= size:
            break
    return total


scores = []
for y, x in visible_positions:
    cnt_left = count_trees(tree_map[y][:x], -1, tree_map[y][x])
    cnt_right = count_trees(tree_map[y][x+1:], 1, tree_map[y][x])
    cnt_up = count_trees([row[x] for row in tree_map[:y]], -1, tree_map[y][x])
    cnt_down = count_trees([row[x] for row in tree_map[y + 1:]], 1, tree_map[y][x])
    scores.append(cnt_left * cnt_right * cnt_up * cnt_down)

print("Result Part 2:", max(scores))
