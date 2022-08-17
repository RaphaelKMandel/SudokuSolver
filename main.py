import numpy as np
from time import time_ns as tic


def check_solved(puzzle):
    if puzzle.sum() == 405:
        return True
    else:
        return False


def get_box(j, i, puzzle):
    slice_x = slice((i // 3) * 3, (i // 3) * 3 + 3, 1)
    slice_y = slice((j // 3) * 3, (j // 3) * 3 + 3, 1)
    box = puzzle[slice_y, slice_x].flatten()
    return box


def find_next_blank(puzzle):
    for row in range(9):
        for col in range(9):
            if puzzle[row, col] == 0:
                return row, col


def solve_puzzle(old_puzzle):
    puzzle = old_puzzle.copy()
    j, i = find_next_blank(puzzle)

    row = puzzle[j, :].tolist()
    col = puzzle[:, i].tolist()
    box = get_box(j, i, puzzle).tolist()
    numbers = row
    numbers.extend(col)
    numbers.extend(box)
    numbers = set(numbers)

    for num in range(1, 10):
        if num not in numbers:
            puzzle[j, i] = num
            #print('New Puzzle')
            #print(puzzle)
            if check_solved(puzzle):
                return puzzle
            else:
                new_puzzle = solve_puzzle(puzzle)
                if check_solved(new_puzzle):
                    return new_puzzle
    return puzzle


puzzle0 = [5, 3, 0, 0, 7, 0, 0, 0, 0,
           6, 0, 0, 1, 9, 5, 0, 0, 0,
           0, 9, 8, 0, 0, 0, 0, 6, 0,
           8, 0, 0, 0, 6, 0, 0, 0, 3,
           4, 0, 0, 8, 0, 3, 0, 0, 1,
           7, 0, 0, 0, 2, 0, 0, 0, 6,
           0, 6, 0, 0, 0, 0, 2, 8, 0,
           0, 0, 0, 4, 1, 9, 0, 0, 5,
           0, 0, 0, 0, 8, 0, 0, 7, 9]


puzzle1 = [0, 0, 0, 0, 0, 0, 0, 0, 8,
           1, 8, 0, 0, 0, 2, 3, 0, 0,
           0, 6, 0, 0, 5, 7, 0, 0, 1,
           0, 7, 0, 9, 6, 0, 0, 0, 0,
           0, 9, 0, 7, 0, 4, 0, 1, 0,
           0, 0, 0, 0, 8, 1, 0, 4, 0,
           6, 0, 0, 2, 4, 0, 0, 8, 0,
           0, 0, 4, 5, 0, 0, 0, 9, 3,
           5, 0, 0, 0, 0, 0, 0, 0, 0]

puzzle2 = np.zeros([9,9],dtype=int).tolist()

puzzle = puzzle2

puzzle = np.array(puzzle).reshape([9,9])
print('Puzzle:')
print(puzzle)
t0 = tic()
solution = solve_puzzle(puzzle)
print('Solution:')
print(solution)
print(f'Solution Time: {(tic()-t0)/1e9} s')
