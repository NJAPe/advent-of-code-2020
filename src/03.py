from common import get_input

START_POS = (0, 0)
PART_1_DIR = (3, 1)
PART_2_DIRS = [
    (1, 1),
    (3, 1),
    (5, 1),
    (7, 1),
    (1, 2),
]

def move(pos, direction, width):
    return (pos[0] + direction[0]) % width , pos[1] + direction[1]

def get_down(inp, pos, direction, impacts=0):
    if pos[1] >= len(inp):
        return impacts
    if inp[pos[1]][pos[0]] == '#':
        impacts += 1
    return get_down(inp, move(pos, direction, len(inp[0])), direction, impacts)

def solve_part_1_test():
    inp = get_input('input\\03_test.txt')
    impacts = get_down(inp, START_POS, PART_1_DIR)
    print(f'Part 1 test: {impacts}')

def solve_part_1():
    inp = get_input('input\\03.txt')
    impacts = get_down(inp, START_POS, PART_1_DIR)
    print(f'Part 1: {impacts}')

def part_2(inp):
    prod = 1
    for direction in PART_2_DIRS:
        prod *= get_down(inp, START_POS, direction)
    return prod

def solve_part_2_test():
    inp = get_input('input\\03_test.txt')
    print(f'Part 2 test: {part_2(inp)}')

def solve_part_2():
    inp = get_input('input\\03.txt')
    print(f'Part 2: {part_2(inp)}')

if __name__ == '__main__':
    solve_part_1_test()
    solve_part_1()
    solve_part_2_test()
    solve_part_2()
