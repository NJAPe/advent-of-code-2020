import string


def get_yesses_set(file_name):
    with open(file_name, 'r') as _f:
        raw = _f.read()
    return [{yes for yes in group if yes != '\n'} for group in raw.split('\n\n')]

def get_groups(file_name):
    with open(file_name, 'r') as _f:
        raw = _f.read()
    return [group.split() for group in raw.split('\n\n')]

def get_all_group_yesses(groups):
    group_yesses = []
    for group in groups:
        all_yesses = string.ascii_lowercase
        for answer in group:
            all_yesses = [i for i in all_yesses if i in answer]
        group_yesses.append(all_yesses)
    return group_yesses

def count_yesses(yesses):
    return [len(yes) for yes in yesses]

def part_2(file_name):
    return count_yesses(get_all_group_yesses(get_groups(file_name)))

def solve_part_1_test():
    num_yes = count_yesses(get_yesses_set('input\\06_test.txt'))
    print(f'Part 1 test: {sum(num_yes)}')

def solve_part_1():
    num_yes = count_yesses(get_yesses_set('input\\06.txt'))
    print(f'Part 1: {sum(num_yes)}')

def solve_part_2_test():
    num_yes = part_2('input\\06_test.txt')
    print(f'Part 2 test: {sum(num_yes)}')

def solve_part_2():
    num_yes = part_2('input\\06.txt')
    print(f'Part 2: {sum(num_yes)}')

if __name__ == "__main__":
    solve_part_1_test()
    solve_part_1()
    solve_part_2_test()
    solve_part_2()

