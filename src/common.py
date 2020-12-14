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
        start = time.perf_counter_ns()
        ret = function(*args, **kwargs)
        stop = time.perf_counter_ns()
        print(f'Execution took {(stop - start)/10**9}s\n')
        return ret
    return wrap

