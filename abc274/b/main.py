#!/usr/bin/env python3
# Author:  + kei
# Date: January 7, 2023

# from helper_classes import *
from collections import *


class Solution:
    '''
    Author:  + kei
    '''

    def solve(self):
        H, W = map(int, input().split())
        g = []
        for _ in range(H):
            g.append(input())

        ans = [0] * W
        for c in range(W):
            for r in range(H):
                if g[r][c] == "#":
                    ans[c] += 1
        print(*ans)


class Try:
    '''
    Author: kei
    '''

    def solve(self):
        H, W = map(int, input().split())


def main():
    # t = Try()
    # t.solve()

    s = Solution()
    s.solve()


if __name__ == '__main__':
    main()
