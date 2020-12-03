from common import get_input

START_POS = (0, 0)
PART_1_DIR = (3, 1)

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

if __name__ == '__main__':
    solve_part_1_test()
    solve_part_1()
