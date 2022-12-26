#!/usr/bin/env python3
# Author:  + kei
# Date: November 26, 2022

# from helper_classes import *
import math
from collections import *


class Solution:
    '''
    Author: kaz_mighty + kei
    '''

    def __init__(self):
        pass

    def solve(self):
        '''
        1. Ternary Search
        '''
        def calc(A, B, g):
            return B * g + A / math.sqrt(g + 1)

        A, B = map(int, input().split())
        left = 0
        right = 10 ** 12
        while right - left > 2:
            mid1 = (left * 2 + right) // 3
            mid2 = (left + right * 2) // 3
            if calc(A, B, mid1) > calc(A, B, mid2):
                left = mid1
            else:
                right = mid2

        ans = min(calc(A, B, left), calc(A, B, left + 1))
        ans = min(ans, calc(A, B, right))
        print('{:.10f}'.format(ans))

    def solve2(self):
        '''
        2. Use differential
        '''
        def calc(A, B, g):
            return B * g + A / math.sqrt(g + 1)

        A, B = map(int, input().split())
        # f'(x) = 0 <=> x = (A / (2 * B)) ** (2 / 3) - 1
        # f(x) is minimum if x = (A / (2 * B)) ** (2 / 3) - 1.
        g = (A / (2 * B)) ** (2 / 3) - 1
        ans = min(calc(A, B, int(g)), calc(A, B, int(g) + 1))
        print('{:.10f}'.format(ans))


class Try:

    def __init__(self):
        pass

    def solve(self):
        from sys import stdin
        input = stdin.readline

        N, M = map(int, input().split())
        A = list(map(int, input().split()))
        for i in range(M):
            for k in range(M):
                if k == i:
                    continue

            print()


def main():
    # t = Try()
    # t.solve()

    s = Solution()
    s.solve()


if __name__ == '__main__':
    main()
