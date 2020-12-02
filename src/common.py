def get_input(filename):
    with open(filename) as _f:
        return _f.read().split('\n')