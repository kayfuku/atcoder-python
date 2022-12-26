#!/usr/bin/env python3
# Author:  + kei
# Date: November 25, 2022

# from helper_classes import *
from collections import *
from sys import stdin
input = stdin.readline


class Solution:

    def __init__(self):
        pass

    def solve(self):

        print()


class Try:

    def __init__(self):
        pass

    def solve(self):

        def recurse(n):
            if n == 0:
                return 1

            if n in dp:
                return dp[n]

            dp[n] = recurse(n // 2) + recurse(n // 3)
            return dp[n]

        N = int(input())
        dp = dict()
        ans = recurse(N)
        print(ans)


def main():
    t = Try()
    t.solve()

    # s = Solution()
    # s.solve()


if __name__ == '__main__':
    main()
