#!/usr/bin/env python3
# Author:  + kei
# Date: December 3, 2022

# from helper_classes import *
from collections import *


class Solution:

    def __init__(self):
        pass

    def solve(self):
        n = int(input())
        s = list(map(int, input().split()))
        ans = []
        before = 0
        for si in s:
            ans.append(si - before)
            before = si
        print(*ans)


class Try:

    def __init__(self):
        pass

    def solve(self):
        N = int(input())
        S = list(map(int, input().split()))
        ans = []
        sum = 0
        for s in S:
            diff = s - sum
            ans.append(diff)
            sum += diff

        print(*ans)


def main():
    # t = Try()
    # t.solve()

    s = Solution()
    s.solve()


if __name__ == '__main__':
    main()
