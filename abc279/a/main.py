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
        print(s.count('v') + s.count('w') * 2)


class Try:

    def __init__(self):
        pass

    def solve(self):
        S = input()
        ans = 0
        for c in S:
            if c == 'v':
                ans += 1
            else:
                ans += 2

        print(ans)


def main():
    t = Try()
    t.solve()

    # s = Solution()
    # s.solve()


if __name__ == '__main__':
    main()
