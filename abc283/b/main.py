#!/usr/bin/env python3
# Author:  + kei
# Date: December 24, 2022

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
        N = int(input())
        A = list(map(int, input().split()))
        Q = int(input())
        for _ in range(Q):
            q = list(map(int, input().split()))
            k = q[1]
            if q[0] == 1:
                x = q[2]
                A[k-1] = x
            else:
                print(A[k-1])


def main():
    t = Try()
    t.solve()

    # s = Solution()
    # s.solve()


if __name__ == '__main__':
    main()
