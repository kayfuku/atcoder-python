#!/usr/bin/env python3
# Author:  + kei
# Date: December 3, 2022

# from helper_classes import *
from collections import *


class Solution:

    def __init__(self):
        pass

    def solve(self):

        print()


class Try:

    def __init__(self):
        pass

    def solve(self):
        H, W = map(int, input().split())
        count = 0
        for i in range(H):
            Si = input()
            count += Si.count('#')

        print(count)


def main():
    t = Try()
    t.solve()

    # s = Solution()
    # s.solve()


if __name__ == '__main__':
    main()
