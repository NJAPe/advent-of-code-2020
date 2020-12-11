from common import get_input


def parse_input(file_name):
    inp = get_input(file_name)
    return [[char for char in row] for row in inp]

def count_total_occupied(seating):
    occupied = 0
    for row in range(len(seating)):
        for seat in seating[row]:
            occupied += seat == '#'
    return occupied

def count_adjacent_occupied(seating, row, column):
    num_occ = 0
    for r in range(max(0, row-1), min(len(seating), row+2)):
        for c in range(max(0, column-1), min(len(seating[r]), column+2)):
            if r == row and c == column:
                continue
            num_occ += seating[r][c] == '#'
    return num_occ

def count_seen_occupied(seating, row, column):
    num_occ = 0
    max_row, max_col = len(seating), len(seating[0])
    for r in range(row-1, row+2):
        for c in range(max(0, column-1), min(max_col, column+2)):
            if r == row and c == column:
                continue
            r_tmp, c_tmp = r, c
            direction = (r-row, c-column)
            while -1 < r_tmp < max_row and -1 < c_tmp < max_col:
                if seating[r_tmp][c_tmp] == '#':
                    num_occ += 1
                    break
                elif seating[r_tmp][c_tmp] == 'L':
                    break
                r_tmp, c_tmp = r_tmp + direction[0], c_tmp + direction[1]
    return num_occ

def iterate_once(seating, occupied_counter, max_adj):
    new_seating = [row.copy() for row in seating]
    changed = False
    for row in range(len(seating)):
        for column in range(len(seating[row])):
            if seating[row][column] == '.':
                continue
            num_occ = occupied_counter(seating, row, column)
            if seating[row][column] == 'L' and num_occ == 0:
                changed = True
                new_seating[row][column] = '#'
            elif seating[row][column] == '#' and num_occ >= max_adj:
                changed = True
                new_seating[row][column] = 'L'
    return new_seating, changed

def solve_part_1(file_name):
    seating, changed = iterate_once(parse_input(file_name), count_adjacent_occupied, 4)
    while changed:
        seating, changed = iterate_once(seating, count_adjacent_occupied, 4)
    num_occ = count_total_occupied(seating)
    print(f'Part 1 {file_name}: {num_occ}')

def solve_part_2(file_name):
    seating, changed = iterate_once(parse_input(file_name), count_seen_occupied, 5)
    while changed:
        seating, changed = iterate_once(seating, count_seen_occupied, 5)
    num_occ = count_total_occupied(seating)
    print(f'Part 2 {file_name}: {num_occ}')

if __name__ == "__main__":
    solve_part_1('input\\11_test.txt')
    solve_part_1('input\\11.txt')
    solve_part_2('input\\11_test.txt')
    solve_part_2('input\\11.txt')
