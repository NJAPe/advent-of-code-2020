from common import get_input

def get_row(inp_row):
    row_raw = inp_row[0:7]
    return int(''.join(['1' if bit == 'B' else '0' for bit in row_raw]), 2)

def get_column(inp_row):
    column_raw = inp_row[7:]
    return int(''.join(['1' if bit == 'R' else '0' for bit in column_raw]), 2)

def get_ids(inp):
    return [get_row(inp_row) * 8 + get_column(inp_row) for inp_row in inp]

def get_my_seat(inp):
    ids = get_ids(inp)
    ids.sort()
    last_non_gap_seat = ids[0]
    for seat_id in ids[1:]:
        if seat_id == last_non_gap_seat + 2:
            return last_non_gap_seat + 1
        last_non_gap_seat = seat_id

def solve_part_1_test():
    inp = get_input('input\\05_test.txt')
    max_id = max(get_ids(inp))
    print(f'Part 1 test: {max_id}')

def solve_part_1():
    inp = get_input('input\\05.txt')
    max_id = max(get_ids(inp))
    print(f'Part 1: {max_id}')

def solve_part_2():
    inp = get_input('input\\05.txt')
    seat = get_my_seat(inp)
    print(f'Part 2: {seat}')

if __name__ == "__main__":
    solve_part_1_test()
    solve_part_1()
    solve_part_2()
