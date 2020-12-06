import string


def part_1(file_name):
    with open(file_name, 'r') as _f:
        raw = _f.read()
    yesses = [{yes for yes in group if yes != '\n'} for group in raw.split('\n\n')]
    return sum([len(yes) for yes in yesses])

def part_2(file_name):
    with open(file_name, 'r') as _f:
        raw = _f.read()
    groups = [group.split() for group in raw.split('\n\n')]
    group_yesses = []
    for group in groups:
        all_yesses = string.ascii_lowercase
        for answer in group:
            all_yesses = [i for i in all_yesses if i in answer]
        group_yesses.append(all_yesses)
    return sum([len(yes) for yes in group_yesses])

def solve_part_1(file_name):
    print(f'{file_name}: {part_1(file_name)}')

def solve_part_2(file_name):
    print(f'{file_name}: {part_2(file_name)}')

if __name__ == "__main__":
    print('Part 1:')
    solve_part_1('input\\06_test.txt')
    solve_part_1('input\\06.txt')
    print('\nPart 2:')
    solve_part_2('input\\06_test.txt')
    solve_part_2('input\\06.txt')
