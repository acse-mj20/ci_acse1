from functools import lru_cache

__all__ = ['my_sum', 'factorial']


def my_sum(iterable):
    total = 0
    for i in iterable:
        total += i
    return total


@lru_cache(maxsize=None)  # Note: -> @cache in python >= 3.9


def factorial(n):
    return n * factorial(n - 1) if n else 1