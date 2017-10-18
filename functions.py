from functools import reduce

# Sum of digits can be found in Basic Syntax/1.py

def multiplication(*args):
    only_ints = filter(lambda x: isinstance(x, int), args)
    return reduce(lambda x, y: x*y, only_ints, 1)
