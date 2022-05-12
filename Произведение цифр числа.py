import functools


def f(n):
    return functools.reduce(lambda x, y: x * y, [int(i) for i in str(n)])
