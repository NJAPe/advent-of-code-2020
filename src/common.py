def get_input(filename):
    with open(filename) as _f:
        return _f.read().split('\n')


def get_int_input(filename):
    with open(filename) as _f:
        return [int(line) for line in _f]
