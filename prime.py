import asyncio
from math import sqrt
import time


async def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(sqrt(x)) + 1):
        if x % i == 0:
            return False
        await asyncio.sleep(0)
    return True


async def print_matches(iterable, async_predicate):
    for item in iterable:
        matches = await async_predicate(item)
        if matches:
            print(f'Found : {item}')


async def repetitive_message(message, interval_seconds):
    while True:
        print(message)
        await asyncio.sleep(interval_seconds)


async def search(iterable, async_predicate):
    for item in iterable:
        if (await async_predicate(item)):
            return item
    raise ValueError('Not Found')


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
