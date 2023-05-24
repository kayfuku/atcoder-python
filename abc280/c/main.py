#!/usr/bin/env python3
# Author:  + kei
# Date: December 3, 2022

# from helper_classes import *
from collections import *
import bisect
from itertools import zip_longest


class Solution:
    '''
    Author: kaz_mighty + kei
    '''

    def __init__(self):
        pass

    def solve(self):
        s = input()
        s += '#'
        t = input()
        for i, si, ti in zip(range(len(s)), s, t):
            if si != ti:
                print(i + 1)
                break


class Try:

    def __init__(self):
        pass

    def solve(self):
        S = input()
        T = input()
        S += '#'
        left = 0
        right = len(T)
        while left < right:
            mid = (left + right) // 2
            if left == mid:
                print(mid + 1)
                return
            if S[left:mid] == T[left:mid]:
                left = mid
            else:
                if left == mid - 1:
                    print(left + 1)
                    return
                right = mid

        return -1

    def solve2(self):
        s = input()
        t = input()
        for i, (si, ti) in enumerate(zip_longest(s, t)):
            if si != ti:
                print(i + 1)
                break


def main():
    t = Try()
    t.solve()
    # t.solve2()

    # s = Solution()
    # s.solve()


if __name__ == '__main__':
    main()
