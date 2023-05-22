#!/usr/bin/env python3
# Author:  + kei
# Date: January 7, 2023

# from helper_classes import *
from collections import *
import numpy as np


class Solution:
    '''
    Author: Kiri8128 + kei
    '''

    def solve(self):
        N = int(input())
        A = list(map(int, input().split()))

        ans = [0] * (2*N+1)
        for i, a in enumerate(A):
            ans[2*i+1] = ans[a-1]+1
            ans[2*i+2] = ans[a-1]+1

        print(*ans, sep="\n")


class Try:
    '''
    Author: kei
    '''

    def solve(self):
        N = int(input())
        A = list(map(int, input().split()))

        print()


def main():
    # t = Try()
    # t.solve()

    s = Solution()
    s.solve()


if __name__ == '__main__':
    main()
