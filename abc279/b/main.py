#!/usr/bin/env python3
# Author:  + kei
# Date: November 26, 2022

# from helper_classes import *
from collections import *


class Solution:
    '''
    Author: kaz_mighty + kei
    '''

    def __init__(self):
        pass

    def solve(self):
        s = input()
        t = input()
        if t in s:
            print('Yes')
        else:
            print('No')


class Try:

    def __init__(self):
        pass

    def solve(self):
        S = input()
        T = input()
        if T in S:
            print('Yes')
        else:
            print('No')


def main():
    # t = Try()
    # t.solve()

    s = Solution()
    s.solve()


if __name__ == '__main__':
    main()
