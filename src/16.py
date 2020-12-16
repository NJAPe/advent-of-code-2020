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

@time_function
def solve_part_1(file_name):
    field_rules, _, nearby_tickets = parse_input(file_name)
    invalid_sum = get_invalid_sum(field_rules, nearby_tickets)
    print(f'Part 1 {file_name}: {invalid_sum}')

if __name__ == "__main__":
    solve_part_1('input\\16_test.txt')
    solve_part_1('input\\16.txt')