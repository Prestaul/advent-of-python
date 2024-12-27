with open('../advent-of-code-inputs/2024/day-02.txt', 'r') as input:
    input = input.read().strip();

example = '''
7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9'''.strip()


def parse_input(input):
    return [[int(x) for x in l.split()] for l in input.splitlines()]

def is_safe(seq):
    prev = seq[0]
    dir = seq[1] - prev
    for val in seq[1:]:
        diff = val - prev
        if (dir > 0) ^ (diff > 0) or abs(diff) < 1 or abs(diff) > 3:
            return False
        prev = val
    return True;

def is_safeish(seq):
    if is_safe(seq):
        return True

    for i in range(len(seq)):
        if (is_safe(seq[:i] + seq[i+1:])):
            return True

    return False

def solve(input):
    return len([x for x in parse_input(input) if is_safe(x)])

def solve2(input):
    return len([x for x in parse_input(input) if is_safeish(x)])

print(solve(example))
print(solve(input))

print(solve2(example))
print(solve2(input))
