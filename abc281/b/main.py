#!/usr/bin/env python3
# Author:  + kei
# Date: December 10, 2022

# from helper_classes import *
from collections import *


class Solution:
    '''
    Author:  + kei
    '''

    def solve(self):
        S = input()
        if len(S) != 8:
            print('No')
            return
        if not ('A' <= S[0] <= 'Z'):
            print('No')
            return
        if S[1] == '0':
            print('No')
            return
        for i in range(2, 7):
            if S[i] not in '0123456789':
                print('No')
                return
        if not ('A' <= S[7] <= 'Z'):
            print('No')
            return

        print('Yes')


class Try:
    '''
    Author: kei
    '''

    def __init__(self):
        pass

    def solve(self):
        S = input()
        if len(S) != 8:
            print('No')
            return
        c1 = S[0]
        if not ('A' <= c1 <= 'Z'):
            print('No')
            return
        num = ''
        for i in range(1, 7):
            if S[i] not in set('0123456789'):
                print('No')
                return
            num += S[i]
        if not (100000 <= int(num) <= 999999):
            print('No')
            return
        c2 = S[7]
        if not ('A' <= c2 <= 'Z'):
            print('No')
            return

        print('Yes')


def main():
    # t = Try()
    # t.solve()

    s = Solution()
    s.solve()


if __name__ == '__main__':
    main()
