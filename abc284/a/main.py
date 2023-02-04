#!/usr/bin/env python3
# Author:  + kei
# Date: January 7, 2023

# from helper_classes import *
from collections import *


class Solution:
    '''
    Author: Kiri8212 + kei
    '''

    def solve(self):
        N = int(input())
        L = [input() for _ in range(N)]
        print('\n'.join(L[::-1]))


class Try:
    '''
    Author: kei
    '''

    def solve(self):
        N = int(input())
        s = []
        for i in range(N):
            S = input()
            s.append(S)

        for i in range(N-1, -1, -1):
            print(s[i])


def main():
    # t = Try()
    # t.solve()

    s = Solution()
    s.solve()


if __name__ == '__main__':
    main()
