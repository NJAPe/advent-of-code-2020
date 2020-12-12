import time

def get_input(filename):
    with open(filename) as _f:
        return _f.read().split('\n')


def get_int_input(filename):
    with open(filename) as _f:
        return [int(line) for line in _f]

def time_function(function):
    def wrap(*args, **kwargs):
        print('\nTiming execution:')
        start = time.time()
        ret = function(*args, **kwargs)
        stop = time.time()
        print(f'Execution took {stop - start}s\n')
        return ret
    return wrap

