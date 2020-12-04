from functools import partial
import re

from common import get_input


def in_range(min, max, actual):
    return min <= int(actual) <= max

def heigt_validator(actual):
    if actual.endswith('cm'):
        return in_range(150, 193, actual[:-2])
    elif actual.endswith('in'):
        return in_range(59, 76, actual[:-2])
    else:
        return False

def haricolor_validator(actual):
    return actual in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']


MANDATORY_KEYS = [
        ('byr', partial(in_range, 1920, 2002)),
        ('iyr', partial(in_range, 2010, 2020)),
        ('eyr', partial(in_range, 2020, 2030)),
        ('hgt', heigt_validator),
        ('hcl', partial(re.fullmatch, r'#[0-9a-z]{6}')),
        ('ecl', haricolor_validator),
        ('pid', partial(re.fullmatch, r'[0-9]{9}')),
    ]

def passport_is_valid(passport, strict):
    
    for (key, validator) in MANDATORY_KEYS:
        if key in passport:
            if strict and not validator(passport[key]):
                return False
        else:
            return False
    return True

def parse_passports(inp):
    passports = [{}]
    for row in inp:
        if row:
            for item in row.split():
                key, val = item.split(':')
                passports[-1][key] = val
        else:
            passports.append({})
    return passports

def get_valid_passport(passports, strict=False):
    return [p for p in passports if passport_is_valid(p, strict)]

def solve_part_1_test():
    inp = get_input('input\\04_test.txt')
    count = len(get_valid_passport(parse_passports(inp)))
    print(f'Part 1 test: {count}')

def solve_part_1():
    inp = get_input('input\\04.txt')
    count = len(get_valid_passport(parse_passports(inp)))
    print(f'Part 1: {count}')

def solve_part_2_test():
    inp = get_input('input\\04_test_2.txt')
    count = len(get_valid_passport(parse_passports(inp), strict=True))
    print(f'Part 2 test: {count}')

def solve_part_2():
    inp = get_input('input\\04.txt')
    count = len(get_valid_passport(parse_passports(inp), strict=True))
    print(f'Part 2: {count}')

if __name__ == '__main__':
    solve_part_1_test()
    solve_part_1()
    solve_part_2_test()
    solve_part_2()
