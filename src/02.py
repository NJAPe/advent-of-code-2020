from common import get_input

def parse_row(row):
    rule_raw, letter, pwd = row.split()
    rule = []
    rule = [int(part) for part in rule_raw.split('-')]
    return rule, letter.strip(':'), pwd

def is_valid_part_1(rule, letter, pwd):
    num_occ = pwd.count(letter)
    return rule[0] <= num_occ and num_occ <= rule[1]

def is_valid_part_2(rule, letter, pwd):
    return (pwd[rule[0] - 1] == letter) ^ (pwd[rule[1] - 1] == letter)

def solve(inp, validator):
    count = 0
    for row in inp:
        row_parts = parse_row(row)
        if validator(*row_parts):
            count += 1
    return count

def solve_part_1_test():
    inp = get_input('input\\02_test.txt')
    print(f'Part 1 test: {solve(inp, is_valid_part_1)}')

def solve_part_1_real():
    inp = get_input('input\\02.txt')
    print(f'Part 1: {solve(inp, is_valid_part_1)}')

def solve_part_2_test():
    inp = get_input('input\\02_test.txt')
    print(f'Part 1 test: {solve(inp, is_valid_part_2)}')

def solve_part_2_real():
    inp = get_input('input\\02.txt')
    print(f'Part 1: {solve(inp, is_valid_part_2)}')



if __name__ == '__main__':
    solve_part_1_test()
    solve_part_1_real()
    solve_part_2_test()
    solve_part_2_real()
