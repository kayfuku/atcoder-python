#!/usr/bin/env python3
# Author:  + kei
# Date: January ?, 2023

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
        T = int(input())
        for t in range(T):
            N = int(input())
            A = list(map(int, input().split()))
            cnt = 0
            for ai in A:
                if ai % 2 == 1:
                    cnt += 1
            print(cnt)


def main():
    t = Try()
    t.solve()

    # s = Solution()
    # s.solve()


if __name__ == '__main__':
    main()
