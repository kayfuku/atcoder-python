#!/usr/bin/env python3
# Author:  + kei
# Date: February ?, 2023

# from helper_classes import *
from collections import *


class Solution:
    '''
    Author:  + kei
    '''

    def solve(self):

        print()


class Try:
    '''
    Author: kei
    '''

    def solve(self):
        N, K = map(int, input().split())
        h = []
        for i in range(K):
            S = input()
            h.append(S)

        h.sort()
        for n in h:
            print(n)


def main():
    t = Try()
    t.solve()

    # s = Solution()
    # s.solve()


if __name__ == '__main__':
    main()
