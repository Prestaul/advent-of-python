import re

with open('../advent-of-code-inputs/2024/day-03.txt', 'r') as input:
    input = input.read().strip();

def solve(input):
    return sum([int(x) * int(y) for x, y in re.findall(r'mul\((\d+),(\d+)\)', input)]);

def solve2(input):
    return solve(re.sub(r"don't\(\).*?do\(\)", 'x', input, flags=re.S))

print(solve('xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))'))
print(solve(input))

print(solve2('xmul(2,4)&mul[3,7]!^don\'t()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))'))
print(solve2(input))
