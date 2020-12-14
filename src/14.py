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

def apply_bitmask2(bitmask, value):
    ret_values = set()
    num_x = bitmask.count('X')
    value = bin(value)[2:]
    value = (36-len(value))*'0' + value
    for variant in range(2**num_x):
        mask_key = bin(variant)[2:]
        mask_key = (num_x-len(mask_key))*'0' + mask_key
        tmp_val = list(value)
        for idx, char in enumerate(bitmask):
            if char == '1':
                tmp_val[idx] = '1'
            elif char == 'X':
                tmp_val[idx] = mask_key[0]
                mask_key = mask_key[1:]
        tmp = int(''.join(tmp_val), 2)
        ret_values.add(tmp)
    return ret_values

def run_program2(inp):
    mem = defaultdict(int)
    bitmask = (0, 2**36-1)
    for row in inp:
        if row.startswith('mask'):
            bitmask = row.split('=')[1].strip()
        else:
            idx, value = row.split('[')[1].split(']')
            values = apply_bitmask2(bitmask, int(idx))
            for val in values:
                mem[val] = int(value.strip(' ='))
    return mem, bitmask

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

def solve_part_2(file_name):
    mem, _ = run_program2(get_input(file_name))
    print(f'Part 2 {file_name}: {sum(mem.values())}')

if __name__ == "__main__":
    solve_part_1('input\\14_test.txt')
    solve_part_1('input\\14.txt')
    solve_part_2('input\\14_test2.txt')
    solve_part_2('input\\14.txt')
