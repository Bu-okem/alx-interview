#!/usr/bin/python3
"""
function to determine the fewest number of
coins needed to meet a given amount total
"""


def makeChange(coins, total):
    """
    function to determine the fewest number of
    coins needed to meet a given amount total
    """
    if total <= 0:
        return 0
    else:
        sorted_coins = sorted(coins)
        sorted_coins.reverse()
        counter = 0
        for coin in sorted_coins:
            while (total >= coin):
                counter += 1
                total -= coin
        if total == 0:
            return counter
        return -1
