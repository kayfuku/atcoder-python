#!/usr/bin/env python3
# Author:  + kei
# Date: November 19, 2022

# from helper_classes import *
from sys import stdin
from collections import *
input = stdin.readline


class Solution:

    def __init__(self):
        pass

    def solve(self):
        '''
        Author: Kiri8128 + kei
        '''
        N = int(input())
        A = [int(a) for a in input().split()]
        last_reset_value = 0
        # Iterate from 1 so that we don't have to worry about the index number.
        diff = defaultdict(int)
        for i, a in enumerate(A, 1):
            diff[i] = a

        Q = int(input())
        for _ in range(Q):
            q = [int(a) for a in input().split()]
            if q[0] == 1:
                # reset
                x = q[1]
                last_reset_value = x
                diff = defaultdict(int)
            elif q[0] == 2:
                # addition
                i, x = q[1:]
                diff[i] += x
            else:
                # output
                i = q[1]
                print(last_reset_value + diff[i])


class Try:

    def solve():
        N = int(input())
        A = list(map(int, input().split()))
        Q = int(input())
        for i in range(Q):
            query = input()


def main():
    # t = Try()
    # t.solve()

    s = Solution()
    s.solve()


if __name__ == '__main__':
    main()
