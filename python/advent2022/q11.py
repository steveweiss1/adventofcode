from functools import reduce
from operator import mul


class Monkey:
    def __init__(self, number, items, op, operand, divisible, true_clause, false_clause):
        self.op = op
        self.false_clause = false_clause
        self.true_clause = true_clause
        self.divisible = divisible
        self.items = items
        self.operand = operand
        self.number = number
        self.inspected = 0

    def add(self, item):
        self.items.append(item)
    def __repr__(self):
        return f'Monkey(number={self.number}, inspected = {self.inspected}, items={self.items}, operand={self.operand}, divisible={self.divisible}, true_clause={self.true_clause}, false_clause={self.false_clause})'

    def __str__(self):
        return f'Monkey {self.number}'


tests = [Monkey(0, [79, 98], '*', 19, 23, 2, 3),
         Monkey(1, [54, 65, 75, 74], '+', 6, 19, 2, 0),
         Monkey(2, [79, 60, 97], '*', 'old', 13, 1, 3),
         Monkey(3, [74], '+', 3, 17, 0, 1)]

real = [Monkey(0, [63, 84, 80, 83, 84, 53, 88, 72], '*', 11, 13, 4, 7),
        Monkey(1, [67, 56, 92, 88, 84], '+', 4, 11, 5, 3),
        Monkey(2, [52], '*', 'old', 2, 3, 1),
        Monkey(3, [59, 53, 60, 92, 69, 72], '+', 2, 5, 5, 6),
        Monkey(4, [61, 52, 55, 61], '+', 3, 7, 7, 2),
        Monkey(5, [79, 53], '+', 1, 3, 0, 6),
        Monkey(6, [59, 86, 67, 95, 92, 77, 91], '+', 5, 19, 4, 0),
        Monkey(7, [58, 83, 89], '*', 19, 17, 2, 1)]

def part1(monkeys):
    for _ in range(20):
        for monkey in monkeys:
            while len(monkey.items) > 0:
                item = monkey.items.pop(0)
                monkey.inspected += 1
                if monkey.op == '*':
                    val = item * (item if monkey.operand == 'old' else int(monkey.operand))
                else:
                    val = item + int(monkey.operand)
                val //= 3
                if val % monkey.divisible == 0:
                    monkeys[monkey.true_clause].add(val)
                else:
                    monkeys[monkey.false_clause].add(val)

    s = sorted(monkeys, key=lambda x: x.inspected, reverse=True)[0:2]
    print(s)
    return s[0].inspected * s[1].inspected

def part2(monkeys):
    divisor_product = int(reduce(mul, (monkey.divisible for monkey in monkeys)))
    for i in range(10000):
        print(i)
        for monkey in monkeys:
            while len(monkey.items) > 0:
                item = monkey.items.pop(0)
                monkey.inspected += 1
                if monkey.op == '*':
                    val = (item * (item if monkey.operand == 'old' else int(monkey.operand))) % divisor_product
                else:
                    val = (item + int(monkey.operand)) % divisor_product
                if val % monkey.divisible == 0:
                    monkeys[monkey.true_clause].add(val)
                else:
                    monkeys[monkey.false_clause].add(val)

    s = sorted(monkeys, key=lambda x: x.inspected, reverse=True)[0:2]
    print(s)
    return s[0].inspected * s[1].inspected

print(part2(real))