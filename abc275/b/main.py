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
        A, B, C, D, E, F = map(int, input().split())
        ans = int((A * B * C - D * E * F) % 998244353)
        print(ans)


def main():
    t = Try()
    t.solve()

    # s = Solution()
    # s.solve()


if __name__ == '__main__':
    main()
