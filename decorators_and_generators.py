def after5(func):
    def wrapper(*args, **kwargs):
        wrapper.called += 1
        if wrapper.called % 5 == 0:
            func(*args, **kwargs)

    wrapper.called = 0
    return wrapper


def memoize(func):
    memo = {}
    def helper(n):
        if n not in memo:
            memo[n] = func(n)
        return memo[n]
    return helper


def fib_non_rec():
    a, b = 1, 1
    while True:
        yield a
        a, b = b, a + b


def accepts(*types):
    def decorator(func):
        def wrapper(*args):
            zip_types = zip(args, types)
            if not all([isinstance(a, b) for a, b in zip_types]):
                raise AttributeError
            func(*args)
        return wrapper
    return decorator


def returns(expected):
    def decorator(func):
        def wrapper(*args):
            result = func(*args)
            if not isinstance(result, expected):
                raise ValueError
        return wrapper
    return decorator
