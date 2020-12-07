from common import get_input

def get_dependencies(inp, include_count=False):
    deps = {}
    for row in inp:
        contain_idx = row.find('contain')
        bag_name = row[:contain_idx-2]
        if 'no other bags.' in row:
            deps[bag_name] = []
        elif include_count:
            deps[bag_name] = {(dep.strip('s. ')[2:], int(dep[0])) for dep in row[contain_idx+8:].split(', ')}
        else:
            deps[bag_name] = {dep.strip('s. ')[2:] for dep in row[contain_idx+8:].split(', ')}
    return deps

def can_bag_contain(bag, dependencies, validated_can, target='shiny gold bag'):
    if target in dependencies[bag]:
        return {bag}
    else:
        for sub_bag in dependencies[bag]:
            if sub_bag in validated_can:
                return {bag, sub_bag}
    for sub_bag in dependencies[bag]:
        sub_bag_contain = can_bag_contain(sub_bag, dependencies, validated_can)
        if sub_bag_contain:
            sub_bag_contain.add(bag)
            return sub_bag_contain
    return set()

def count_internal_bags(bag, dependencies):
    if not dependencies[bag]:
        return 0
    else:
        tot_sub_bags = 0
        for sub_bag, count in dependencies[bag]:
            tot_sub_bags += count * (count_internal_bags(sub_bag, dependencies) + 1)
        return tot_sub_bags


def solve_part_1(input_file):
    inp = get_input(input_file)
    dependencies = get_dependencies(inp)
    validated_can = set()
    for bag in dependencies:
        validated_can = validated_can.union(can_bag_contain(bag, dependencies, validated_can))
    print(f'Part 1 {input_file}: {len(validated_can)}')

def solve_part_2(input_file):
    inp = get_input(input_file)
    dependencies = get_dependencies(inp, include_count=True)
    print(f'Part 2 {input_file}: {count_internal_bags("shiny gold bag", dependencies)}')

if __name__ == "__main__":
    solve_part_1('input\\07_test.txt')
    solve_part_1('input\\07.txt')
    solve_part_2('input\\07_test.txt')
    solve_part_2('input\\07_test2.txt')
    solve_part_2('input\\07.txt')
