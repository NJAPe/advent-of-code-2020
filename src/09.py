from common import get_input


def parse_input(file_name):
    return [int(i) for i in get_input(file_name)]

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
    idx = preamble
    while idx < len(inp):
        if has_sum(inp[idx - preamble:idx], inp[idx]):
            idx += 1
        else:
            return inp[idx]


def get_contiguos_sum_to(numbers, target):
    tail, head = 0, 1
    contiguos = [numbers[tail]]
    while True:
        contiguos.append(numbers[head])
        curr_sum = sum(contiguos)
        if curr_sum == target:
            return contiguos
        elif  curr_sum < target:
            head += 1
            if head == len(numbers):
                raise ValueError('Not possible to make sum')
        else:
            tail += 1
            head = tail + 1
            contiguos = [numbers[tail]]
    return None

def solve_part_1(file_name, preamble):
    missing = get_first_missing(parse_input(file_name), preamble)
    print(f'Part 1 {file_name}: {missing}')

def solve_part_2(file_name, preamble):
    inp = parse_input(file_name)
    missing = get_first_missing(inp, preamble)
    contiguos = sorted(get_contiguos_sum_to(inp, missing))
    print(f'Part 2 {file_name}: {contiguos[0] + contiguos[-1]}')

if __name__ == "__main__":
    solve_part_1('input\\09_test.txt', 5)
    solve_part_1('input\\09.txt', 25)
    solve_part_2('input\\09_test.txt', 5)
    solve_part_2('input\\09.txt', 25)
