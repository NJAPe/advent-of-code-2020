from common import get_input

def east(pos, rot, amount):
    return (pos[0] + amount, pos[1]), rot

def west(pos, rot, amount):
    return (pos[0] - amount, pos[1]), rot

def north(pos, rot, amount):
    return (pos[0], pos[1] + amount), rot

def south(pos, rot, amount):
    return (pos[0], pos[1] - amount), rot

def right(pos, rot, amount):
    return pos, (rot + amount) % 360

def left(pos, rot, amount):
    return pos, (rot - amount) % 360

def forward(pos, rot, amount):
    f = None
    if rot == 0:
        f = north
    elif rot == 90:
        f = east
    elif rot == 180:
        f = south
    elif rot == 270:
        f = west
    else:
        raise ValueError(f'currently not supported move rotated {amount} degrees')
    return f(pos, rot, amount)

def rotate_waypoint(pos, degrees):
    if degrees % 90 != 0:
        raise ValueError(f'Cant rotate {degrees}degrees')
    for _ in range(int((degrees % 360) / 90)):
        pos = pos[1], -pos[0]
    return pos

COMMANDS = {
    'E': east,
    'W': west,
    'N': north,
    'S': south,
    'L': left,
    'R': right,
    'F': forward,
}

def do_moves(inp, rotation):
    pos = (0, 0)
    for row in inp:
        pos, rotation = COMMANDS[row[0]](pos, rotation, int(row[1:]))
    return pos

def do_moves_waypoint(inp, waypoint_pos):
    pos = (0, 0)
    for row in inp:
        cmd = row[0]
        arg = int(row[1:])
        if cmd in ('E', 'W', 'N', 'S'):
            waypoint_pos, _ = COMMANDS[cmd](waypoint_pos, 0, arg)
        elif cmd == 'L':
            waypoint_pos = rotate_waypoint(waypoint_pos, -arg)
        elif cmd == 'R':
            waypoint_pos = rotate_waypoint(waypoint_pos, arg)
        elif cmd == 'F':
            pos = pos[0] + arg * waypoint_pos[0], pos[1] + arg * waypoint_pos[1]
        else:
            raise ValueError(f'What exactly do you mean with "{cmd}"')
    return pos

def manhattan_dist(pos):
    return abs(pos[0]) + abs(pos[1])

def solve_part_1(file_name):
    pos = do_moves(get_input(file_name), 90)
    print(f'Part 1 {file_name}: {manhattan_dist(pos)}')

def solve_part_2(file_name):
    pos = do_moves_waypoint(get_input(file_name), (10, 1))
    print(f'Part 2 {file_name}: {manhattan_dist(pos)}')

if __name__ == "__main__":
    solve_part_1('input\\12_test.txt')
    solve_part_1('input\\12.txt')
    solve_part_2('input\\12_test.txt')
    solve_part_2('input\\12.txt')