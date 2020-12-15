from collections import defaultdict

from common import get_input, time_function


def play_game(row, end_round):
    start_numbers = [int(i.strip()) for i in row.split(',')]
    numbers = defaultdict(int)
    for idx, num in enumerate(start_numbers[:-1]):
        numbers[num] = idx + 1
    prev_number = start_numbers [-2]
    next_number = start_numbers [-1]
    round_num = len(start_numbers)
    while round_num <= end_round:
        prev_number = next_number
        next_number = 0
        if numbers[prev_number] != 0:
            next_number = round_num - numbers[prev_number]
        numbers[prev_number] = round_num
        round_num += 1
    return numbers, prev_number

def solve_part_1(file_name):
    _ , last_number = play_game(get_input(file_name)[0], 2020)
    print(f'Part 1 {file_name}: {last_number}')

@time_function
def solve_part_2(file_name):
    _ , last_number = play_game(get_input(file_name)[0], 30000000)
    print(f'Part 2 {file_name}: {last_number}')

if __name__ == "__main__":
    solve_part_1('input\\15_test.txt')
    solve_part_1('input\\15.txt')
    solve_part_2('input\\15_test.txt')
    solve_part_2('input\\15.txt')
