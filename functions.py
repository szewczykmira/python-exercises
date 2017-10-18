from functools import reduce
import itertools

# Sum of digits can be found in Basic Syntax/1.py

def multiplication(*args):
    only_ints = filter(lambda x: isinstance(x, int), args)
    return reduce(lambda x, y: x*y, only_ints, 1)


def longer_than(min_len, *strings):
    return [string for string in strings if len(string) > min_len]


def groupby(fun, *elems):
    result = {}
    for key, value in itertools.groupby(elems, fun):
        value = list(value)
        current_val = result.get(key, [])
        current_val.extend(value)
        result.update({key: current_val})
    return result
