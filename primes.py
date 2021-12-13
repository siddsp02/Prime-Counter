# !usr/bin/env python3

"""Counts the number of primes from 2 to a user-specified limit.
A number is considered prime if it is greater than or equal to 2,
and its only factors are 1 and itself.
"""

import cProfile
import pstats
from math import isqrt

__author__ = "Siddharth (Sidd) Pai"
__email__ = "sidd.s.pai@gmail.com"


def count_primes(limit: int) -> int:
    """Counts the number of primes from 2 to the limit, and returns the result."""

    primes = [2, 3]

    if limit <= 1:
        raise ValueError("limit has to be greater than or equal to 2.")

    if limit in primes:
        return limit - 1

    def is_prime(n: int) -> bool:

        if not n % (s := isqrt(n)):
            return False

        i = 1
        j = primes[i]

        while j < s:
            if not n % j:
                return False
            i += 1
            j = primes[i]

        primes.append(n)

        return True

    for i in range(5, limit, 2):
        is_prime(i)

    return len(primes)


def main(n: int = 100_000) -> None:
    with cProfile.Profile() as pr:
        result = count_primes(n)
        print(result)
        pr.print_stats(pstats.SortKey.TIME)


if __name__ == "__main__":
    main()
