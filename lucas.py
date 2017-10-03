def lucas():
    a = 2
    b = 1
    yield a
    while True:
        yield b
        a, b = b, a + b


def fib():
    a = 0
    b = 1
    while True:
        yield a
        a, b = b, a + b


def async_search(iterable, predicate):
    for item in iterable:
        if predicate(item):
            return item
        yield
    raise ValueError('Not Found')
