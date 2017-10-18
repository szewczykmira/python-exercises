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


@memoize
def fib(n):
    print("fib({})".format(n))
    if n <= 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)

@after5
def test():
    print('Yo!')


def fib_non_rec():
    a, b = 1, 1
    while True:
        yield a
        a, b = b, a + b
