def after5(func):
    def wrapper(*args, **kwargs):
        wrapper.called += 1
        if wrapper.called % 5 == 0:
            func(*args, **kwargs)

    wrapper.called = 0
    return wrapper


@after5
def test():
    print('Yo!')
