import re
import math

input_data = open('day5.txt').read()

def part1(input_data):
    page_ordering, updates = input_data.split('\n\n')
    ordering = {}
    
    for pair in page_ordering.split('\n'):
        x, y = pair.split('|')
        if ordering.get(x) is None:
            ordering[x] = [y]
        else:
            ordering[x].append(y)

    total = 0

    for update in [l.split(',') for l in updates.split('\n')]:
        correct = True
        for i in range(len(update)):
            if not correct:
                break
            for j in range(i+1, len(update)):
                if (ordering.get(update[i]) is not None and update[j] not in ordering[update[i]]) or (ordering.get(update[j]) is not None and update[i] in ordering[update[j]]):
                    correct = False
        if correct:
            total += int(update[len(update)//2])

    return total

def part2(input_data):
    page_ordering, updates = input_data.split('\n\n')
    ordering = {}
    
    for pair in page_ordering.split('\n'):
        x, y = pair.split('|')
        if ordering.get(x) is None:
            ordering[x] = [y]
        else:
            ordering[x].append(y)

    total = 0

    for update in [l.split(',') for l in updates.split('\n')]:
        corrected = False
        for i in range(len(update)):
            for j in range(i+1, len(update)):
                if (ordering.get(update[i]) is not None and update[j] not in ordering[update[i]]) or (ordering.get(update[j]) is not None and update[i] in ordering[update[j]]):
                    corrected = True
                    update[i], update[j] = update[j], update[i]
        if corrected:
            # print(update)
            total += int(update[len(update)//2])
    
    return total

print("Part 1:", part1(input_data))
print("Part 2:", part2(input_data))