from common import get_input


def has_sum(numbers, target):
    numbers.sort()
    start, stop = 0, len(numbers) - 1
    while start < stop and numbers[start] != numbers[stop]:
        cur_sum = numbers[start] + numbers[stop]
        if target == cur_sum:
            return True
        elif cur_sum < target:
            start += 1
        else:
            stop -= 1
    return False

def get_first_missing(inp, preamble):
    inp = [int(i) for i in inp]
    idx = preamble
    while idx < len(inp):
        if has_sum(inp[idx - preamble:idx], inp[idx]):
            idx += 1
        else:
            return inp[idx]

def solve_part_1(file_name, preamble):
    missing = get_first_missing(get_input(file_name), preamble)
    print(f'Part 1 {file_name}: {missing}')

if __name__ == "__main__":
    solve_part_1('input\\09_test.txt', 5)
    solve_part_1('input\\09.txt', 25)
