#!/usr/bin/python3
"""This module define a single function makeChange
"""
from typing import List


def makeChange(coins: List[int], total: int) -> int:
    """Finds the minimum number of coins to make a target total
    """
    if total <= 0:
        return 0

    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    for coin in coins:
        for sub_value in range(coin, total + 1):
            dp[sub_value] = min(dp[sub_value], dp[sub_value - coin] + 1)

    return dp[total] if dp[total] != float('inf') else -1
