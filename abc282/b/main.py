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
        N, M = map(int, input().split())
        p = [input() for _ in range(N)]

        cnt = 0
        for i in range(N):
            for j in range(i+1, N):
                for mi in range(M):
                    if p[i][mi] == 'x' and p[j][mi] == 'x':
                        break
                else:
                    cnt += 1

        print(cnt)


class Try:
    '''
    Author: kei
    '''

    def __init__(self):
        pass

    def solve(self):
        N, M = map(int, input().split())
        p = []
        for i in range(N):
            Si = input()
            p.append(Si)

        # print(p)
        cnt = 0
        flag = True
        for i in range(N):
            for j in range(i + 1, N):
                flag = True
                for mi in range(M):
                    if p[i][mi] == 'x' and p[j][mi] == 'x':
                        flag = False
                        break
                if flag:
                    cnt += 1

        print(cnt)


def main():
    # t = Try()
    # t.solve()

    s = Solution()
    s.solve()


if __name__ == '__main__':
    main()
