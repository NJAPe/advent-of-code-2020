from common import get_input

from collections import defaultdict

def get_bitmask(value):
    or_mask = 36*['0']
    and_mask = 36*['1']
    for idx, bit in enumerate(value):
        if bit == 'X':
            continue
        elif bit == '1':
            or_mask[idx] = '1'
        else:
            and_mask[idx] = '0'
    return int(''.join(or_mask), 2), int(''.join(and_mask), 2)

def apply_bitmask(bitmask, value):
    return (value | bitmask[0]) & bitmask[1]

def run_program(inp):
    mem = defaultdict(int)
    bitmask = (0, 2**36-1)
    for row in inp:
        if row.startswith('mask'):
            bitmask = get_bitmask(row.split('=')[1].strip())
        else:
            idx, value = row.split('[')[1].split(']')
            mem[idx] = apply_bitmask(bitmask, int(value.strip(' =')))
    return mem, bitmask

def solve_part_1(file_name):
    mem, _ = run_program(get_input(file_name))
    print(f'Part 1 {file_name}: {sum(mem.values())}')

if __name__ == "__main__":
    solve_part_1('input\\14_test.txt')
    solve_part_1('input\\14.txt')
