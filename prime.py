from math import sqrt
import time


def async_sleep(interval_seconds):
    start = time.time()
    expire = start + interval_seconds
    while True:
        yield
        now = time.time()
        if now >= expire:
            break


def async_is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(sqrt(x)) + 1):
        if x % i == 0:
            return False
        yield from async_sleep(0)
    return True


def async_print_matches(iterable, async_predicate):
    for item in iterable:
        matches = yield from async_predicate(item)
        if matches:
            print(f'Found : {item}')


def async_repetitive_message(message, interval_seconds):
    while True:
        print(message)
        yield from async_sleep(interval_seconds)


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


def async_search(iterable, async_predicate):
    for item in iterable:
        if (yield from async_predicate(item)):
            return item
    raise ValueError('Not Found')
