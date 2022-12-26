#!/usr/bin/env python3
# Author:  + kei
# Date: November 26, 2022

# from helper_classes import *
from collections import *


class Solution:
    '''
    TODO: ?
    '''

    def __init__(self):
        pass

    def solve(self):
        n, m = map(int, input().split())
        a = list(map(int, input().split()))
        a.append(0)
        desc = list(range(1, n + 1))
        for i in range(m - 1, 0, -1):
            ai = a[i] - 1
            desc[ai], desc[ai + 1] = desc[ai + 1], desc[ai]
        asc = list(range(1, n + 1))
        index = 0
        for i in range(m):
            ai = a[i] - 1
            print(desc[index])
            if ai == index:
                index += 1
            elif ai + 1 == index:
                index -= 1
            asc[ai], asc[ai + 1] = asc[ai + 1], asc[ai]
            next_ai = a[i + 1] - 1
            desc[next_ai], desc[next_ai + 1] = desc[next_ai + 1], desc[next_ai]


class Try:

    def __init__(self):
        pass

    def solve(self):
        N, K = map(int, input().split())
        A = list(map(int, input().split()))

        print()


def main():
    # t = Try()
    # t.solve()

    s = Solution()
    s.solve()


if __name__ == '__main__':
    main()
