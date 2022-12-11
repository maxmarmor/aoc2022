#!/usr/bin/python3
from dataclasses import dataclass, field
import copy

with open("input.txt", "r") as f:
    puzzle_input = f.read()

Input: list[str] = puzzle_input.split("\n\n")


@dataclass
class Monkey:
    test_divisor: int
    cnt_inspections: int = 0
    operand: int = 0
    operation: str = ""
    items: list[int] = field(default_factory=list)
    target_monkeys: list = field(default_factory=list)  # [a, b] - a: false, b: true cases

    def process(self, base_monkeys, worry_div: int = None):
        for item in self.items:
            this_operand = self.operand if self.operand else item
            new_item = item + this_operand if self.operation == "+" else item * this_operand
            if worry_div:
                new_item = (new_item - self.test_divisor) % worry_div + self.test_divisor
            else:
                new_item = new_item // 3
            self.throw_to_monkey(
                self.target_monkeys[int(self.test(new_item))],
                new_item,
                base_monkeys)
            self.cnt_inspections += 1
        self.items = []

    def test(self, item: int):
        return item % self.test_divisor == 0

    def throw_to_monkey(self, target_monkey, item: int, base_monkeys):
        base_monkeys[target_monkey].items.append(item)


monkeys: list[Monkey] = []

for dataset in Input:
    dataset = dataset.split("\n")
    operand = 0 if dataset[2].split("= ")[-1].split(" ")[2] == "old" else int(dataset[2].split("= ")[-1].split(" ")[2])
    monkeys.append(Monkey(
        items=list(map(int, dataset[1].split(": ")[-1].split(", "))),
        operation=dataset[2].split("= ")[-1].split(" ")[1],
        operand=operand,
        test_divisor=int(dataset[3].split(" ")[-1]),
        target_monkeys=[int(dataset[5].split(" ")[-1]), int(dataset[4].split(" ")[-1])]
    ))

monkeys_part1 = copy.deepcopy(monkeys)
for _ in range(20):
    for monkey in monkeys_part1:
        monkey.process(monkeys_part1)

inspections = list(reversed(sorted([monkey.cnt_inspections for monkey in monkeys_part1])))
print("Result Part 1:", inspections[0] * inspections[1])

# Part 2
monkeys_part2 = copy.deepcopy(monkeys)

worry_divisor = 1
for monkey in monkeys_part2:
    worry_divisor *= monkey.test_divisor if monkey.test_divisor else 1
    for el in monkey.items:
        worry_divisor *= el

for _ in range(10000):
    for monkey in monkeys_part2:
        monkey.process(monkeys_part2, worry_divisor)

inspections = sorted([monkey.cnt_inspections for monkey in monkeys_part2])
print("Result Part 2:", inspections[-1] * inspections[-2])
