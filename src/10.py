from common import get_int_input
from collections import defaultdict


def get_num_diffs(inp):
    inp.sort()
    inp.append(inp[-1] + 3)
    counts = {1:0, 2:0, 3:0}
    prev = 0
    for rating in inp:
        counts[rating-prev] += 1
        prev = rating
    return counts

def get_consecutive_run_from(inp, idx):
    consecutive = [inp[idx]]
    for i in inp[idx + 1:]:
        if i > consecutive[-1] + 1:
            break
        else:
            consecutive.append(i)
    return consecutive

def num_path_in_consecutive(consecutive):
    length = len(consecutive)
    if length == 1:
        return 1
    elif length == 2:
        return 1
    elif length == 3:
        return 2
    else:
        a, b, c = 1, 1, 2
        for _ in range(length - 3):
            a, b, c = b, c, a + b + c
        return c

def get_num_ways(inp, idx, consecutive):
    if consecutive[-1] == inp[-1]:
        return num_path_in_consecutive(consecutive)
    next_consecutive = get_consecutive_run_from(inp, idx + len(consecutive))
    path_in_cons = num_path_in_consecutive(consecutive)
    return path_in_cons * get_num_ways(inp, idx + len(consecutive), next_consecutive)

def solve_part_1(file_name):
    counts = get_num_diffs(get_int_input(file_name))
    print(f'Part 1 {file_name}: {counts[1]*counts[3]}')

def solve_part_2(file_name):
    inp = get_int_input(file_name)
    inp.append(0)
    inp.sort()
    counts = get_num_ways(inp, 0, get_consecutive_run_from(inp, 0))
    print(f'Part 2 {file_name}: {counts}')

if __name__ == "__main__":
    solve_part_1('input\\10_test.txt')
    solve_part_1('input\\10.txt')
    solve_part_2('input\\10_test.txt')
    solve_part_2('input\\10.txt')
