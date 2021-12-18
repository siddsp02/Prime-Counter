# !usr/bin/env python3

"""Counts the number of primes from 2 to a user-specified limit.
A number is considered prime if it is greater than or equal to 2,
and its only factors are 1 and itself.
"""

import cProfile
import pstats
from math import isqrt


def count_primes(limit: int) -> int:
    """Returns the number of primes from 2 to the limit specified."""
    primes = set(range(3, limit + 1, 2))
    for i in range(3, isqrt(limit) + 1, 2):
        if i in primes:
            primes.difference_update(range(i ** 2, limit + 1, i))
    return len(primes) + 1


def main(n: int = 100_000) -> None:
    with cProfile.Profile() as pr:
        print(count_primes(n))
        pr.print_stats(pstats.SortKey.TIME)


if __name__ == "__main__":
    main(250_000)
