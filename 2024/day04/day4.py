import re
import math

input_data = open("day4.txt").read()

arr = ['X', 'M', 'A', 'S']

def check_diagonals(i, j, matrix):
    # top
    num = 0
    if i >= 3:
        if j >= 3:
            num += check_diag(i, j, -1, -1, matrix)
        if j <= len(matrix[i]) - 4:
            num += check_diag(i, j, -1, 1, matrix)
    if i <= len(matrix) - 4:
        if j >= 3:
            num += check_diag(i, j, 1, -1, matrix)
        if j <= len(matrix[i]) - 4:
            num += check_diag(i, j, 1, 1, matrix)
    return num


def check_diag(i, j, idir, jdir, matrix):
    k = 1
    while k < 4:
        if matrix[i+k*idir][j+k*jdir] != arr[k]:
            break
        k += 1
    return 1 if k == 4 else 0

def part1(input_data):
    total = 0
    matrix = [[c for c in l] for l in input_data.split('\n')]
    # check horizontal
    for l in input_data.split('\n'):
        total += len(re.findall(r'(XMAS)', l))
        total += len(re.findall(r'(SAMX)', l))
    # check vertical
    inv = list(zip(*matrix[::-1]))
    for l in [''.join(c) for c in inv]:
        total += len(re.findall(r'(XMAS)', l))
        total += len(re.findall(r'(SAMX)', l))
    # check diagonals
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 'X':
                total += check_diagonals(i, j, matrix)
    
    return total
    
def check_x(i, j, matrix):
    if i == 0 or i == len(matrix)-1 or j == 0 or j == len(matrix[i])-1:
        return 0
    
    forw = False
    back = False

    if matrix[i+1][j+1] == 'S':
        if matrix[i-1][j-1] == 'M':
            back = True
    elif matrix[i+1][j+1] == 'M':
        if matrix[i-1][j-1] == 'S':
            back = True

    if matrix[i+1][j-1] == 'S':
        if matrix[i-1][j+1] == 'M':
            forw = True
    elif matrix[i+1][j-1] == 'M':
        if matrix[i-1][j+1] == 'S':
            forw = True

    return 1 if forw and back else 0

def part2(input_data):
    total = 0
    matrix = [[c for c in l] for l in input_data.split('\n')]

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 'A':
                total += check_x(i,j,matrix)

    return total


print("Part 1:", part1(input_data))
print("Part 2:", part2(input_data))