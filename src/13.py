from common import get_input
from math_utils import chinese_remainder


def parse_input(file_name, keep_x=False):
    inp = get_input(file_name)
    time_stamp = int(inp[0])
    busses = [bus for bus in inp[1].split(',') if bus != 'x' or keep_x]
    return time_stamp, busses

def parse_input_2(file_name):
    inp = get_input(file_name)
    busses, idx = [], []
    for i, bus in enumerate(inp[1].split(',')):
        if bus != 'x':
            busses.append(int(bus))
            idx.append(int(bus) - i)
    return busses, idx

def get_departure(earliest, bus):
    bus_num = int(bus)
    if earliest % bus_num == 0:
        return earliest
    else:
        return (earliest // bus_num + 1) * bus_num

def get_departures(time_stamp, busses):
    departures = {get_departure(time_stamp,bus): bus for bus in busses}
    return departures

def solve_part_1(file_name):
    time_stamp, busses = parse_input(file_name)
    departures = get_departures(time_stamp, busses)
    earliest_departure = min(departures.keys())
    ans = (earliest_departure - time_stamp) * int(departures[earliest_departure])
    print(f'Part 1 {file_name}: {ans}')

def solve_part_2(file_name):
    busses, idx = parse_input_2(file_name)
    time = chinese_remainder(busses, idx)
    print(f'Part 2 {file_name}: {time}')

if __name__ == "__main__":
    solve_part_1('input\\13_test.txt')
    solve_part_1('input\\13.txt')
    solve_part_2('input\\13_test.txt')
    solve_part_2('input\\13.txt')
