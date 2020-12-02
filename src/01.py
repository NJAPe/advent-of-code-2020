from common import get_input

def solve_part_1(inp):
    temp = {}
    for row in inp:
        num = int(row)
        if num in temp:
            return num * temp[num]
        else:
            temp[2020-num] = num

def solve_part_1_test():
    ans = solve_part_1(get_input('input\\01_test.txt'))
    print(f'Part 1 test answer is: {ans}')

def solve_part_1_real():
    ans = solve_part_1(get_input('input\\01.txt'))
    print(f'Part 1 answer is: {ans}')

def solve_part_2(inp):
    sums = {}
    inp_num = [int(i) for i in inp]
    for idx, num_1 in enumerate(inp_num):
        for num_2 in inp_num[idx + 1:]:
            sums[num_1 + num_2] = num_1 * num_2

    for num_3 in inp_num:
        if (2020 - num_3) in sums:
            return num_3 * sums[2020 - num_3]

def solve_part_2_test():
    ans = solve_part_2(get_input('input\\01_test.txt'))
    print(f'Part 2 test answer is: {ans}')

def solve_part_2_real():
    ans = solve_part_2(get_input('input\\01.txt'))
    print(f'Part 2 test answer is: {ans}')

def main():
    solve_part_1_test()
    solve_part_1_real()
    solve_part_2_test()
    solve_part_2_real()

if __name__ == '__main__':
    main()
