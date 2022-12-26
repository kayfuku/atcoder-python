#!/usr/bin/env python3
# Author: tk727 + kei
# Date: November 19, 2022
from collections import defaultdict
import sys
input = sys.stdin.readline


def solve():
    N, M = map(int, input().split())

    g = [[] for _ in range(N + 1)]
    for _ in range(M):
        A, B = map(int, input().split())
        g[A].append(B)
        g[B].append(A)

    for i in range(1, N + 1):
        nei = g[i]
        nei.sort()
        print(len(nei), *nei)


def main():
    solve()


if __name__ == '__main__':
    main()
