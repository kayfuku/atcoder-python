#!/usr/bin/env python3
# Author:  + kei
# Date: December 17, 2022

# from helper_classes import *
from collections import *


class Solution:
    '''
    Author: tk727 + kei
    '''

    def __init__(self):
        pass

    def solve(self):
        K = int(input())
        ans = ''
        for i in range(K):
            ans += chr(ord('A') + i)
        print(ans)


class Try:
    '''
    Author: kei
    '''

    def __init__(self):
        pass

    def solve(self):
        K = int(input())
        ans = []
        for c in range(ord('A'), ord('A')+K):
            ans.append(chr(c))

        print(''.join(ans))


def main():
    t = Try()
    t.solve()

    # s = Solution()
    # s.solve()


if __name__ == '__main__':
    main()
