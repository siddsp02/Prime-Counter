# !usr/bin/env python3

"""Counts the number of primes from 2 to a user-specified limit.
A number is considered prime if it is greater than or equal to 2,
and its only factors are 1 and itself.
"""

import cProfile
import pstats
from math import isqrt
from itertools import takewhile

__author__ = "Siddharth (Sidd) Pai"
__email__ = "sidd.s.pai@gmail.com"


def count_primes(limit: int) -> int:
    """Returns the number of primes from 2 to the limit specified."""

    if limit <= 1:
        return 0

    if limit in (primes := [2, 3]):
        return limit - 1

    def is_prime(n: int) -> None:
        if not n % (s := isqrt(n)):
            return

        for prime in primes:
            if not n % prime:
                return
            if s < prime:
                break

        primes.append(n)

    for i in range(5, limit, 2):
        is_prime(i)

    return len(primes)


def main(n: int = 100_000) -> None:
    with cProfile.Profile() as pr:
        result = count_primes(n)
        print(result)
        pr.print_stats(pstats.SortKey.TIME)


if __name__ == "__main__":
    main(250_000)
