#!/usr/bin/python3
"""This kodule define the isWinner amd other helper functions
"""


def isWinner(x, nums):
    """Define the Prime game
    """

    def sieve_of_eratosthenes(n):
        primes = [True] * (n + 1)
        primes[0] = primes[1] = False
        for i in range(2, int(n ** 0.5) + 1):
            if primes[i]:
                for j in range(i * i, n + 1, i):
                    primes[j] = False
        return [i for i in range(n + 1) if primes[i]]

    def can_win(n):
        primes = sieve_of_eratosthenes(n)
        if n in primes:
            return True
        return False

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if can_win(n):
            if n % 2 == 0:
                maria_wins += 1
            else:
                ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
