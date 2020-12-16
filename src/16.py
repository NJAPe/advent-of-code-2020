from common import time_function

def parse_ticket(ticket):
    return [int(field) for field in ticket.split(',')]

def parse_input(file_name):
    with open(file_name) as _f:
        raw_in = _f.read()
    fields_r, my_ticket_r, nearby_tickets_r = raw_in.split('\n\n')
    field_rules = dict()
    for row in fields_r.split('\n'):
        name, ranges_r = row.split(':')
        ranges = []
        for r in ranges_r.split('or'):
            f, t = r.strip().split('-')
            ranges.append((int(f), int(t)))
        field_rules[name.strip()] = ranges
    my_ticket = parse_ticket(my_ticket_r.split('\n')[1])
    nearby_tickets = [parse_ticket(ticket) for ticket in nearby_tickets_r.split('\n')[1:]]
    return field_rules, my_ticket, nearby_tickets

def is_field_valid(value, field_rules):
    for ruleset in field_rules.values():
        for valid_range in ruleset:
            if valid_range[0] <= value <= valid_range[1]:
                return True
    return False

def get_invalid_sum(field_rules, nearby_tickets):
    invalid = dict()
    for ticket in nearby_tickets:
        for field in ticket:
            if field in invalid:
                invalid[field] += 1
            elif not is_field_valid(field, field_rules):
                invalid[field] = 1
    invalid_sum = 0
    for key, value in invalid.items():
        invalid_sum += key * value
    return invalid_sum

def get_valid_tickets(field_rules, nearby_tickets):
    valid_tickets = []
    invalid = dict()
    for ticket in nearby_tickets:
        is_valid = True
        for field in ticket:
            if field in invalid:
                invalid[field] += 1
            elif not is_field_valid(field, field_rules):
                is_valid = False
                break
        if is_valid:
            valid_tickets.append(ticket)
    return valid_tickets

def find_field_positions(field_rules, valid_tickets):
    potential_fields = {field_names:{i for i in range(len(field_rules))} for field_names in field_rules.keys()}
    for field_name, rules in field_rules.items():
        for i in range(len(field_rules)):
            all_ok = True
            for ticket in valid_tickets:
                if not is_field_valid(ticket[i], {field_name: rules}):
                    all_ok = False
                    break
            if not all_ok:
                potential_fields[field_name].remove(i)
    known_fields = dict()
    while len(known_fields) < len(field_rules):
        found_field = None
        for field, possibilities in potential_fields.items():
            if len(possibilities) == 1:
                found_field = field
                break
        if not field:
            raise RuntimeError('Could not match all fields')
        known_fields[found_field] = potential_fields[found_field].pop()
        potential_fields.pop(found_field, None)
        for p in potential_fields.values():
            p.remove(known_fields[found_field])
    return known_fields

def get_ticket_product(known_fields, ticket, prefix):
    prod = 1
    for field, idx in known_fields.items():
        if field.startswith(prefix):
            prod *= ticket[idx]
    return prod


@time_function
def solve_part_1(file_name):
    field_rules, _, nearby_tickets = parse_input(file_name)
    invalid_sum = get_invalid_sum(field_rules, nearby_tickets)
    print(f'Part 1 {file_name}: {invalid_sum}')

@time_function
def solve_part_2(file_name, prefix='departure'):
    field_rules, my_ticket, nearby_tickets = parse_input(file_name)
    valid_tickets = get_valid_tickets(field_rules, nearby_tickets)
    known_fields = find_field_positions(field_rules, valid_tickets)
    print(f'Part 2 {file_name}: {get_ticket_product(known_fields, my_ticket, prefix)}')

if __name__ == "__main__":
    solve_part_1('input\\16_test.txt')
    solve_part_1('input\\16.txt')
    solve_part_2('input\\16_test2.txt', '')
    solve_part_2('input\\16.txt')