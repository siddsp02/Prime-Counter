# !usr/bin/env python3

"""Script for checking whether an integer n is prime or not.
Optimized for high performance.
"""

import cProfile
import pstats
import time
from functools import cache
from math import isqrt

__author__ = "Siddharth (Sidd) Pai"
__email__ = "sidd.s.pai@gmail.com"


@cache
def is_prime(n: int) -> bool:
    """Returns the truth value of whether a number is prime."""

    if n == 2 or n == 3:
        return True

    if not n & 1 or n <= 1:
        return False

    if not n % (s := isqrt(n)):
        return False

    for i in filter(is_prime, range(3, s, 2)):
        if not n % i:
            return False

    return True


def main() -> None:
    with cProfile.Profile(timer=time.perf_counter, builtins=False) as pr:
        # Check for the number of primes <= 250,000
        primes = 0
        for i in range(2, 250_001):
            primes += is_prime(i)
        pr.print_stats(pstats.SortKey.TIME)


if __name__ == "__main__":
    main()
