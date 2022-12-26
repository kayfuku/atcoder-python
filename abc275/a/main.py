#!/usr/bin/env python3
# Author:  + kei
# Date: November 25, 2022

# from helper_classes import *
from collections import *
# from sys import stdin
# input = stdin.readline


class Solution:

    def __init__(self):
        pass

    def solve(self):

        print()


class Try:

    def __init__(self):
        pass

    def solve(self):
        N = int(input())
        H = list(map(int, input().split()))
        max_h = H[0]
        max_idx = 0
        for i in range(1, N):
            if H[i] > max_h:
                max_h = H[i]
                max_idx = i

        print(max_idx + 1)


def main():
    t = Try()
    t.solve()

    # s = Solution()
    # s.solve()


if __name__ == '__main__':
    main()
