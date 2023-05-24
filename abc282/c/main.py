#!/usr/bin/env python3
# Author:  + kei
# Date: December 17, 2022

# from helper_classes import *
from collections import *


class Solution:
    '''
    Author: kaz_mighty + kei
    '''

    def __init__(self):
        pass

    def solve(self):
        N = int(input())
        S = input()
        ans = []
        f = False
        for i in range(N):
            if S[i] == '"':
                # Toggle.
                f ^= True
            if S[i] == ',' and not f:
                ans.append('.')
            else:
                ans.append(S[i])

        print(''.join(ans))


class Try:
    '''
    Author: kei
    '''

    def __init__(self):
        pass

    def solve(self):
        N = int(input())
        S = input()
        ans = []
        cnt = 0
        for c in S:
            if c == '"':
                cnt += 1
            if c == ',' and cnt % 2 == 0:
                ans.append('.')
            else:
                ans.append(c)

        print(''.join(ans))


def main():
    t = Try()
    t.solve()

    # s = Solution()
    # s.solve()


if __name__ == '__main__':
    main()
