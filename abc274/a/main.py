#!/usr/bin/env python3
# Author:  + kei
# Date: January 7, 2023

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
        '''
        decimal numbers with zero padding
        '''
        A, B = map(int, input().split())
        ans = B / A
        print('{:#.3f}'.format(ans))


def main():
    t = Try()
    t.solve()

    # s = Solution()
    # s.solve()


if __name__ == '__main__':
    main()
