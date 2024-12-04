import re

input_data = open("day3.txt").read()

mul_regex = r'mul\((\d+),(\d+)\)'

def part1(input_data):
    total = 0
    for x, y in re.findall(mul_regex, input_data):
        total += int(x) * int(y)
    return total

def part2(input_data):
    total = 0
    do_regex = r'(?:do\(\)|^)(.*?)(?:don\'t\(\)|$)'
    for s in re.findall(do_regex, input_data.replace('\n','')):
        for x, y in re.findall(mul_regex, s):
            total += int(x) * int(y)
    return total

print("Part 1:", part1(input_data))
print("Part 2:", part2(input_data))

# Both parts in a single line of code for funsies
# sum([int(x)*int(y) for x, y in re.findall(r'mul\((\d+),(\d+)\)', open("day3.txt").read())])
# sum([int(x)*int(y) for x, y in re.findall(r'mul\((\d+),(\d+)\)', ''.join(re.findall(r'(?:do\(\)|^)(.*?)(?:don\'t\(\)|$)', open("day3.txt").read().replace('\n',''))))])