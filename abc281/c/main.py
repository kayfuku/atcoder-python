#!/usr/bin/env python3
# Author:  + kei
# Date: December 10, 2022

# from helper_classes import *
from collections import *


class Solution:
    '''
    Author:  + kei
    '''

    def __init__(self):
        pass

    def solve(self):
        N, T = map(int, input().split())
        A = list(map(int, input().split()))
        s = sum(A)
        t = T % s
        for i, a in enumerate(A):
            if a > t:
                # This tune.
                print(i + 1, t)
                break
            # t >= a
            # Get rest.
            t -= a


class Try:
    '''
    Author: kei
    '''

    def __init__(self):
        pass

    def solve(self):
        N, T = map(int, input().split())
        A = list(map(int, input().split()))
        sum_ = sum(A)
        t = T % sum_
        cum_sum = 0
        prev_cum_sum = 0
        for i, ai in enumerate(A):
            cum_sum += ai
            if t // cum_sum == 0:
                print(i + 1, t % prev_cum_sum if i != 0 else t)
                return
            prev_cum_sum = cum_sum


def main():
    # t = Try()
    # t.solve()

    s = Solution()
    s.solve()


if __name__ == '__main__':
    main()
