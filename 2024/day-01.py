with open('../advent-of-code-inputs/2024/day-01.txt', 'r') as input:
    input = input.read().strip();

example = """
3   4
4   3
2   5
1   3
3   9
3   3""".strip()

def parse_input(input):
    return [sorted(col) for col in zip(*[[int(x) for x in l.split()] for l in input.splitlines()])]

def solve(input):
    a, b = parse_input(input)
    return sum([abs(a - b) for a, b in zip(a, b)])

def solve2(input):
    a, b = parse_input(input)
    return sum([a * b.count(a) for a in a])

print(solve(example))
print(solve(input))

print(solve2(example))
print(solve2(input))
