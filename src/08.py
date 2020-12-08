from common import get_input

def parse_program_line(line):
    cmd, arg = line.split()
    return cmd, int(arg)

def run_program(program):
    acc, prg_cnt = 0, 0
    executed_lines = set()
    while prg_cnt not in executed_lines and prg_cnt < len(program):
        executed_lines.add(prg_cnt)
        cmd, arg = parse_program_line(program[prg_cnt])
        if cmd == 'nop':
            prg_cnt += 1
        elif cmd == 'acc':
            acc += arg
            prg_cnt += 1
        elif cmd == 'jmp':
            prg_cnt += arg
        else:
            raise ValueError(f'Unknown cmd "{cmd}" on line {prg_cnt}')
    return acc, prg_cnt

def swap_jmp_nop(program, line_nmbr):
    if 'jmp' in program[line_nmbr]:
        program[line_nmbr] = f'nop{program[line_nmbr][3:]}'
        return True
    elif 'nop' in program[line_nmbr]:
        program[line_nmbr] = f'jmp{program[line_nmbr][3:]}'
        return True
    else:
        return False

def solve_part_1(file_name):
    acc, _ = run_program(get_input(file_name))
    print(f'Part 1 {file_name}: {acc}')

def solve_part_2(file_name):
    program = get_input(file_name)
    mod_line, acc, prg_cnt = 0, 0, 0
    while mod_line <= len(program):
        if swap_jmp_nop(program, mod_line):
            acc, prg_cnt = run_program(program)
            if prg_cnt >= len(program):
                break
            else:
                swap_jmp_nop(program, mod_line)
        mod_line += 1
    if prg_cnt < len(program):
        raise ValueError('No resolution found')
    print(f'Part 1 {file_name}: {acc}')

if __name__ == "__main__":
    solve_part_1('input\\08_test.txt')
    solve_part_1('input\\08.txt')
    solve_part_2('input\\08_test.txt')
    solve_part_2('input\\08.txt')