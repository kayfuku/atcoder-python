#!/usr/bin/env python3
# Author: tk727 + kei
# Date: November 19, 2022

# from helper_classes import *
from collections import *
import sys
input = sys.stdin.readline


class Solution:

    def __init__(self):
        pass

    def solve(self):
        N, Q = map(int, input().split())
        g = defaultdict(set)
        for _ in range(Q):
            T, A, B = map(int, input().split())
            if T == 1:
                g[A].add(B)
            elif T == 2:
                if B in g[A]:
                    g[A].remove(B)
            else:
                if A in g[B] and B in g[A]:
                    print('Yes')
                else:
                    print('No')


class Try:

    def solve(self):
        N, Q = map(int, input().split())
        g = defaultdict(set)
        for i in range(Q):
            T, A, B = map(int, input().split())
            A -= 1
            B -= 1
            if T == 1:
                g[A].add(B)
            if T == 2:
                if B in g[A]:
                    g[A].remove(B)
            if T == 3:
                if B in g[A] and A in g[B]:
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
