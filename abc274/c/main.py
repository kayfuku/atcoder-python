#!/usr/bin/env python3
# Author:  + kei
# Date: January 7, 2023

# from helper_classes import *
from collections import *


class Solution:
    '''
    Author: Kiri8128 + kei
    '''

    def solve(self):
        N = int(input())
        A = list(map(int, input().split()))
        gen = [0] * (2 * N + 2)
        for i, a in enumerate(A):
            gen[2*i] = gen[a] + 1
            gen[2*i+1] = gen[a] + 1

        for g in range(1, len(gen)):
            print(g)


class Try:
    '''
    Author: kei
    '''

    def solve(self):
        N = int(input())
        A = list(map(int, input().split()))

        print()


def main():
    t = Try()
    t.solve()

    # s = Solution()
    # s.solve()


if __name__ == '__main__':
    main()
