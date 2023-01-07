#!/usr/bin/env python3
# Author:  + kei
# Date: December 24, 2022

# from helper_classes import *
from collections import *


class Solution:
    '''
    Author: kaz_mighty + kei
    '''

    def solve(self):
        s = input()
        print(len(s) - s.count('00'))


class Try:
    '''
    Author: kei
    '''

    def solve(self):
        S = str(input())
        n_double_o = 0
        n = len(S)
        f = False
        for i in range(n):
            if S[i] == '0' and not f:
                f = True
            elif S[i] == '0' and f:
                n_double_o += 1
                f = False
            elif S[i] != '0':
                f = False

        print(n - n_double_o)


def main():
    # t = Try()
    # t.solve()

    s = Solution()
    s.solve()


if __name__ == '__main__':
    main()
